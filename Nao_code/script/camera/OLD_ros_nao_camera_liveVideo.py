import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image , CompressedImage
from sensor_msgs.msg import CameraInfo


def callback(data):
    #rospy.loginfo(data)
    img = bridge.imgmsg_to_cv2(data,desired_encoding="bgr8")

   # img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    face = face_cascade.detectMultiScale(img, 1.1, 4)

    print(len(face))
    for(x,y,w,h) in face:
      cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.namedWindow("face detect", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("face detect",1200,1000)
    cv2.imshow("face detect",img)
    cv2.waitKey(2)

# /nao_robot/camera/bottom/camera/camera_info


def main():
    rospy.init_node("bottom_camera_info_listener",anonymous=True)
    # rospy.init_node("bottom_camera_raw_listener",anonymous=True)

    # rospy.Subscriber("/nao_robot/camera/front/camera/image_raw",Image,callback=callback)
    # rospy.Subscriber("/nao_robot/camera/top/camera/image_raw",Image,callback=callback)
    rospy.Subscriber("/naoqi_driver/camera/front/image_raw",Image,callback=callback)
    rospy.spin()


if __name__=="__main__":
    bridge = CvBridge()
    face_cascade = cv2.CascadeClassifier('/home/haoyi/Documents/study/ros_nao/script/camera/haarcascade_frontalface_default.xml')
    main()
