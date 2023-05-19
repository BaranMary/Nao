import rospy
# import nao_robot
from dynamic_reconfigure.msg import Config
from dynamic_reconfigure.msg import ConfigDescription

def callback(data):
    rospy.loginfo('get from callback')
    rospy.loginfo(data)


def main():
    """ * /nao_robot/microphone/naoqi_microphone/get_loggers
        * /nao_robot/microphone/naoqi_microphone/set_logger_level
        * /nao_robot/microphone/naoqi_microphone/set_parameters """
    rospy.init_node('audio_updater')
    # service = rospy.ServiceProxy('/nao_robot/microphone/naoqi_microphone/get_loggers', nao_robot.microphone.naoqi_microphone.get_loggers)
    sub = rospy.Subscriber("/nao_speech/parameter_descriptions", ConfigDescription, callback)
    rospy.spin()

if __name__=="__main__":
    main()