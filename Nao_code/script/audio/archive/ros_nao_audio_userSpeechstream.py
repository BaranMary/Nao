import rospy
from naoqi_bridge_msgs.msg import AudioBuffer
import scipy.io.wavfile as wavf
import numpy as np
import pyaudio
import struct
import deepspeech
""" @misc{github,
  author={ awesomebytes },
  title={ nao_audio_to_audio_common},
  year={2014},
  url={https://github.com/awesomebytes/nao_audio_to_audio_common/blob/master/scripts/play_stream.py},
} """

class ros_nao_audio_streamPlay():
    def __init__(self):
        rospy.loginfo("Getting audio card...")
        self.p = pyaudio.PyAudio()
        # Open stream
        self.stream = self.p.open(format=pyaudio.paInt16, channels=4, rate=16000, output=True,frames_per_buffer=4096)
        rospy.loginfo("Done!")
        # the setting (format, channels, rate) can be done only once (and should only most probably)
        rospy.loginfo("Setting up subscriber to " +"/nao_robot/microphone/naoqi_microphone/audio_raw")
        self.sub = rospy.Subscriber("/nao_robot/microphone/naoqi_microphone/audio_raw", AudioBuffer, self.audio_cb)
        rospy.loginfo("Done!")
        

    def audio_cb(self, msg):

        rospy.loginfo("Callback received!")
        # Start stream
        self.stream.start_stream()

        # Write to stream
        dataBuff = bytes(struct.pack("<{}h".format(len(msg.data)), *msg.data))
        self.stream.write(dataBuff)


if __name__=="__main__":
    rospy.init_node('play_audio_msgs')
    
    PNAT = ros_nao_audio_streamPlay()
    rospy.spin()

