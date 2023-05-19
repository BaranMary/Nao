import rospy
import face_recognition
import cv2
import numpy as np
import sqlite3 as sql
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import String

db_path = './userinfo.db'


class change_user_arrays():
    def __init__(self):
        # self.name_array = np.array([])
        self.name_array = []

    def default_name_array(self):
        # self.name_array = np.array([])
        self.name_array = []


class face_recog():
    def __init__(self):
        rostopic_name = '/naoqi_driver/camera/front/image_raw'
        conn = sql.connect(db_path, check_same_thread=False)

        self.face_cascade = cv2.CascadeClassifier(
            '/home/haoyi/Documents/study/ros_nao/script/camera/haarcascade_frontalface_default.xml')
        self.font = cv2.FONT_HERSHEY_DUPLEX
        self.c = conn.cursor()
        self.bridge = CvBridge()
        self.iden = change_user_arrays()
        self.username = "New User"
        rospy.init_node("face_recog", anonymous=True)
        rospy.loginfo("--------init the 'face_rocog' node--------")
        rospy.Subscriber(rostopic_name, Image, callback=self.callback)
        rospy.spin()

    def callback(self, data):
        frame = self.bridge.imgmsg_to_cv2(data, desired_encoding="bgr8")

        num_face = self.face_count(frame)

        if num_face != 0:
            if self.username == 'New User':
                self.face_compare(frame)
                # compare 15 times
                cur_frame = self.draw_face(frame)
            else:
                cur_frame = self.draw_face(frame)
        else:
            cur_frame = frame
            self.username = "New User"


        cv2.namedWindow("face detect", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("face detect", 1200, 1000)
        cv2.imshow("face detect", cur_frame)
        cv2.waitKey(2)

    def face_count(self, frame):
        # face = self.face_cascade.detectMultiScale(frame, 1.1, 4)
        face_locations = face_recognition.face_locations(frame)

        return len(face_locations)

    def draw_face(self, frame):
        face = self.face_cascade.detectMultiScale(frame, 1.1, 4)

        for(x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (216, 91, 56), 1)
            # cv2.rectangle(rgb_frame, (left, top), (right, bottom), (216,91,56), 1)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (x, y+h), (x+w, y+h+17),
                          (216, 91, 56), cv2.FILLED)
            cv2.putText(frame, self.username, (x + 1, y+h+15),
                        self.font, 0.4, (0, 204, 255), 1)


        # face_locations = face_recognition.face_locations(frame)

        # for (top, right, bottom, left), name in zip(face_locations, self.username):
        #         # Draw a box around the face
        #         cv2.rectangle(frame, (left-10, top-10), (right+10, bottom+10), (216,91,56), 1)
        #         # Draw a label with a name below the face
        #         cv2.rectangle(frame, (left, bottom - 15), (right, bottom), (216,91,56), cv2.FILLED)
        #         cv2.putText(frame, self.username, (left + 6, bottom - 6), self.font, 0.4, (0,204, 255), 1)

        return frame

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

    def face_compare(self, rgb_frame):
        known_user_name, known_user_features = self.read_db()
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            name = "New User"
            if(len(known_user_features) != 0):
                matches = face_recognition.compare_faces(
                    known_user_features, face_encoding, tolerance=0.48)
                face_distances = face_recognition.face_distance(
                    known_user_features, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_user_name[best_match_index]
            face_names.append(name)
            self.iden.name_array.append(name)
            # process_this_frame = not process_this_frame
        if len(self.iden.name_array) >= 15:
            publisher = rospy.Publisher("userChanged", String, queue_size=15)
            msg_string = String()
            temp = np.array(self.iden.name_array)
            unique, pos = np.unique(temp, return_inverse=True)
            counts = np.bincount(pos)
            maxpos = counts.argmax()
            msg_string.data = unique[maxpos]
            publisher.publish(msg_string)
            rospy.loginfo('sending current user name: '+msg_string.data)
            self.username = msg_string.data
            self.iden.default_name_array()


if __name__ == '__main__':
    run = face_recog()
