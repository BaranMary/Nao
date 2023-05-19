import rospy
from std_msgs.msg import String, Bool
import subprocess


def camera_callback(data):
    rospy.loginfo("get from callback")
    print("-------------1111111111111111111-------------")
    # file_path = '/home/haoyi/Documents/study/ros_nao/'
    # ttsSay = data.data.replace("\n","")

    # cmd = 'conda run -n py2 python '+file_path +'ros_nao_AnimatedSpeech.py --a False --s'
    # cmd = cmd.split()
    # cmd.append(ttsSay)
    # # print(cmd)
    # subprocess.Popen(cmd)



def main():
    # m.ALAnimatedSpeech()
    rospy.init_node('test')
    rospy.Subscriber("/userLeft",Bool,callback=camera_callback)
    rospy.spin()

if __name__=="__main__":
    main()
