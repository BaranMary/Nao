import rospy
import face_recognition
import cv2
import numpy as np
import sqlite3 as sql
from cv_bridge import CvBridge
from sensor_msgs.msg import Image , CompressedImage
from sensor_msgs.msg import CameraInfo 
from std_msgs.msg import String

db_path = './userinfo.db'

class change_user_arrays():
    def __init__(self):
        # self.name_array = np.array([])
        self.name_array = []

    def default_name_array(self):
        # self.name_array = np.array([])
        self.name_array = []

def callback(data):
    # rospy.loginfo("--------subscrib to /naoqi_driver/camera/top/image_raw --------")
    
    frame = bridge.imgmsg_to_cv2(data,desired_encoding="bgr8")

    # |||||||||||||||||||||||||||||
    # read from userinfo.db
    conn = sql.connect(db_path,check_same_thread=False)
    # print("finished db connect")
    c = conn.cursor()
    known_user_name=np.array(c.execute("select username from userinfo").fetchall()).flatten()
    temp_feature=np.array(c.execute("select feature_array from userinfo").fetchall()).flatten()
    conn.close()
    # recover = np.fromstring(ss.strip('[]'), dtype=np.float64, sep=',')
    known_user_features = []
    # print(temp_feature.shape)
    for i in range(len(temp_feature)):
        cur = np.fromstring(temp_feature[i].strip('[]'), dtype=np.float64, sep=',')
        # print(cur,i)
        known_user_features.append(cur)
    # known_user_features = np.array()
    # |||||||||||||||||||||||||||||

    show_frame = face_recog(frame, known_user_features,known_user_name,iden)

    cv2.namedWindow("face detect", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("face detect",800,800)
    cv2.imshow("face detect",show_frame)
    cv2.waitKey(2)

def face_recog(rgb_frame,known_user_features,known_user_name,iden,process_this_frame=True):

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    # print(len(face_encodings))
    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        # matches = face_recognition.compare_faces(known_user_features, face_encoding,tolerance=0.5)
        name = "New User"

        # Or instead, use the known face with the smallest distance to the new face
        if(len(known_user_features)!=0):
            matches = face_recognition.compare_faces(known_user_features, face_encoding,tolerance=0.52)

            face_distances = face_recognition.face_distance(known_user_features, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_user_name[best_match_index]


        face_names.append(name)
        iden.name_array.append(name)
        process_this_frame = not process_this_frame
    if len(iden.name_array)>=15:
        publisher = rospy.Publisher("userChanged",String,queue_size=15)
        msg_string = String()
        temp = np.array(iden.name_array)
        unique,pos = np.unique(temp,return_inverse=True)
        counts = np.bincount(pos) 
        maxpos = counts.argmax() 
        msg_string.data = unique[maxpos]
        publisher.publish(msg_string)
        rospy.loginfo('sending current user name')  
        iden.default_name_array()

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):

        # Draw a box around the face
        cv2.rectangle(rgb_frame, (left, top), (right, bottom), (216,91,56), 1)

        # Draw a label with a name below the face
        cv2.rectangle(rgb_frame, (left, bottom - 25), (right, bottom), (216,91,56), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(rgb_frame, name, (left + 6, bottom - 6), font, 0.8, (0,204, 255), 1)
    return rgb_frame


def main():
    # rospy.loginfo("--------init the 'face_rocog' node--------")
    rospy.init_node("face_recog",anonymous=True)
    rospy.loginfo("--------init the 'face_rocog' node--------")

    rospy.loginfo("--------subscrib to /naoqi_driver/camera/top/image_raw --------")
    rospy.Subscriber(rostopic_name,Image,callback=callback)
    rospy.spin()

if __name__=='__main__':
    bridge = CvBridge()
    rostopic_name = '/naoqi_driver/camera/front/image_raw'
    # rostopic_name='/usb_cam/image_raw'
    iden = change_user_arrays()
    main()