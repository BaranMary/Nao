import rospy
import face_recognition
import cv2
import numpy as np
import sqlite3 as sql
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import String, Bool

db_path = './userinfo.db'


class identify_user_arrays():
    def __init__(self):
        self.face_boolean_array = []
        self.userExist_boolean_array = []

    def default_face_bool(self):
        self.face_boolean_array = []

    def default_exist_bool(self):
        self.userExist_boolean_array = []


class face_recog():
    def __init__(self):
        rostopic_name = '/naoqi_driver/camera/front/image_raw'
        self.conn = sql.connect(db_path, check_same_thread=False)
        self.learn_rate = 80
        self.userleft = False
        self.c = self.conn.cursor()
        self.bridge = CvBridge()
        self.iden = identify_user_arrays()
        self.username = "New User"

        self.pub = rospy.Publisher('/temp', String, queue_size=1000) 
        rospy.loginfo("--------init the 'face_rocog' node--------")
        rospy.init_node("face_learn", anonymous=True)
        rospy.Subscriber(rostopic_name, Image, callback=self.callback)
        rospy.spin()

    def callback(self, data):
        frame = self.bridge.imgmsg_to_cv2(data, desired_encoding="bgr8")

        num_face = self.face_count(frame)

        if num_face != 0:
            if self.username == 'New User':
                self.face_recog(frame)
        else:
            face_locations = face_recognition.face_locations(frame)
            self.if_userLeft(face_locations)
            if self.userleft:
                self.username = "New User"
                self.userleft = False

 

    def face_count(self, frame):
        face  = face_recognition.face_locations(frame)
        return len(face)

    def read_db(self):

        known_user_name = np.array(self.c.execute(
            "select username from userinfo").fetchall()).flatten()
        temp_feature = np.array(self.c.execute(
            "select feature_array from userinfo").fetchall()).flatten()
        known_user_features = []
        for i in range(len(temp_feature)):
            cur = np.fromstring(temp_feature[i].strip(
                '[]'), dtype=np.float64, sep=',')
            known_user_features.append(cur)
        return known_user_name, known_user_features

    def if_userLeft(self,face_locations):
        # Find all the faces and face encodings in the current frame of video
        
        if len(face_locations) == 0:
            self.iden.userExist_boolean_array.append(False)
            if len(self.iden.userExist_boolean_array) >= 28:  # 4~5 secs
                self.iden.default_exist_bool()
                print("User has Left")
                publisher = rospy.Publisher("userLeft", Bool, queue_size=1)
                msg_string = Bool()
                msg_string.data = True
                publisher.publish(msg_string)
                rospy.loginfo('sending userLeft True to ros_nao_dialog')
                self.userleft = True

    def face_recog(self, rgb_frame):
        known_user_name, known_user_features = self.read_db()
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            name = "New User"
            # Or instead, use the known face with the smallest distance to the new face
            if(len(known_user_features) != 0):
                matches = face_recognition.compare_faces(known_user_features, face_encoding, tolerance=0.48)
                face_distances = face_recognition.face_distance(known_user_features, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_user_name[best_match_index]
            print(len(self.iden.face_boolean_array))
            if name == "New User":
                self.iden.face_boolean_array.append(False)
                self.iden.default_exist_bool()
            else:
                self.iden.face_boolean_array.append(True)
                self.iden.default_exist_bool()

        if len(self.iden.face_boolean_array) >= 15:
            # Use portion 1:2 instead of OR
            # True == 1, False == 0
            portion = sum(self.iden.face_boolean_array)
            self.iden.default_face_bool()
            if portion <= 6:
                # need to learn this face
                msg_string = String()
                msg_string.data = "Hello New User, I am learning your face right now, Please wait to input your name."
                self.pub.publish(msg_string)

                new_user_feature, name = self.feature_learning(rgb_frame, model='large')
                rospy.loginfo("Finish extracting face feature")
                new_user_feature = np.array2string(new_user_feature[0], separator=',')
                new_user_feature = new_user_feature.replace('\n', '')
                self.c.execute("insert into userinfo values (?,?,?,?)",(name, new_user_feature, 'NULL', 'NULL'))
                self.conn.commit()
                self.username = name

    def feature_learning(self, frame, model='large'):
        rospy.loginfo("starting extract face feature")
        # publisher = rospy.Publisher('/temp', String, queue_size=1000) 
        # msg_string = String()
        # msg_string.data = "Hello New User, I am learning your face right now, Please wait to input your name."
        # publisher.publish(msg_string)
        # rospy.Rate(10).sleep()
        face_encoding = face_recognition.face_encodings(frame, num_jitters=self.learn_rate, model='large')
        name = 'New User'
        name = input('Welcome! Please input your name: ')

        while self.name_check(name):
            name = input('Please input your name except "new user": ')

        return face_encoding, name
    
    def name_check(self,name):
        cooked_name = name.replace(' ','').lower()
        if cooked_name=='newuser':
            return True
        return False




if __name__ == '__main__':

    run = face_recog()
