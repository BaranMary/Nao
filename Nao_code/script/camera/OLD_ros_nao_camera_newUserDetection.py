import rospy
import face_recognition
import cv2
import numpy as np
import sqlite3 as sql
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CompressedImage
from sensor_msgs.msg import CameraInfo
from std_msgs.msg import Bool

db_path = './userinfo.db'


class identify_user_arrays():
    def __init__(self):
        self.face_boolean_array = []
        self.userExist_boolean_array = []

    def default_face_bool(self):
        self.face_boolean_array = []

    def default_exist_bool(self):
        self.userExist_boolean_array = []


def callback(data):
    # rospy.loginfo("------ come from newUserDetection !!! ------")
    frame = bridge.imgmsg_to_cv2(data, desired_encoding="bgr8")

    # |||||||||||||||||||||||||||||
    # read from userinfo.db
    conn = sql.connect(db_path, check_same_thread=False)
    # print("finished db connect")
    c = conn.cursor()
    known_user_name = np.array(
        c.execute("select username from userinfo").fetchall()).flatten()
    temp_feature = np.array(
        c.execute("select feature_array from userinfo").fetchall()).flatten()
    conn.close()
    # recover = np.fromstring(ss.strip('[]'), dtype=np.float64, sep=',')
    known_user_features = []
    # print(temp_feature.shape)
    for i in range(len(temp_feature)):
        cur = np.fromstring(temp_feature[i].strip(
            '[]'), dtype=np.float64, sep=',')
        # print(cur,i)
        known_user_features.append(cur)
    # known_user_features = np.array()
    # |||||||||||||||||||||||||||||

    show_frame = face_recog(frame, known_user_features, known_user_name, iden)


def face_recog(rgb_frame, known_user_features, known_user_name, iden, process_this_frame=True):

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    if len(face_encodings) == 0:
        iden.userExist_boolean_array.append(False)
        if len(iden.userExist_boolean_array) >= 28:  # 4~5 secs
            iden.default_exist_bool()
            print("User has Left")
            publisher = rospy.Publisher("userLeft", Bool, queue_size=1)
            msg_string = Bool()
            msg_string.data = True
            publisher.publish(msg_string)
            rospy.loginfo('sending userLeft True to ros_nao_dialog')
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        name = "New User"
        # Or instead, use the known face with the smallest distance to the new face
        if(len(known_user_features) != 0):
            matches = face_recognition.compare_faces(
                known_user_features, face_encoding, tolerance=0.52)
            face_distances = face_recognition.face_distance(
                known_user_features, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_user_name[best_match_index]
        print(len(iden.face_boolean_array))
        if name == "New User":
            iden.face_boolean_array.append(False)
            iden.default_exist_bool()
        else:
            iden.face_boolean_array.append(True)
            iden.default_exist_bool()

    if len(iden.face_boolean_array) >= 15:
        # Use portion 1:2 instead of OR
        # True == 1, False == 0
        portion = sum(iden.face_boolean_array)
        iden.default_face_bool()
        if portion <= 6:
            # need to learn this face
            new_user_feature, name = feature_learning(
                rgb_frame, face_locations[0], model='large')
            if name != "New User":
                rospy.loginfo("Finish extracting face feature")
                new_user_feature = np.array2string(
                    new_user_feature[0], separator=',')
                # print(new_user_feature)
                new_user_feature = new_user_feature.replace('\n', '')
                # print(new_user_feature)
                conn = sql.connect(db_path, check_same_thread=False)
                # print("finished db connect")
                c = conn.cursor()
                c.execute("insert into userinfo values (?,?,?,?)",
                          (name, new_user_feature, 'NULL', 'NULL'))
                conn.commit()
                conn.close()
    return rgb_frame


def feature_learning(frame, location, num_jitters=500, model='large'):

    # face_locations = face_recognition.face_locations(frame)
    rospy.loginfo("starting extract face feature")
    # print("location : " + str(location[0]))
    # face_encoding = face_recognition.face_encodings(frame, location,num_jitters=num_jitters,model=model)
    face_encoding = face_recognition.face_encodings(
        frame, num_jitters=50, model='large')
    name = 'New User'
    name = input('Welcome! Please input your name: ')
    return face_encoding, name


def main():
    rospy.loginfo("--------init the 'face_rocog' node--------")
    rospy.init_node("face_learn", anonymous=True)
    # publisher = rospy.Publisher("chatter",String,queue_size=10)
    # rospy.loginfo("--------subscrib to /naoqi_driver/camera/top/image_raw --------")
    rospy.Subscriber(rostopic_name, Image, callback=callback)
    rospy.spin()


if __name__ == '__main__':
    bridge = CvBridge()
    print("Start db connect")
    rostopic_name = '/naoqi_driver/camera/front/image_raw'
    # print(len(face_boolean_array))
    iden = identify_user_arrays()

    main()
