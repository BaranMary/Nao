import rospy
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

class ros_nao_audio_service():
    def __init__(self):
        rospy.Service('nao_recordAudio', MySrvFile, callback_function)

        

    def audio_cb(self, msg):
        rospy.loginfo("Callback received!")
        # Start stream
        temp = list(msg.data)
        self.audioRawData.append(temp)
        # Write to stream
        dataBuff = bytes(struct.pack("<{}h".format(len(msg.data)), *msg.data))

        # Decode the audio data
        data_array = np.array(self.audioRawData, dtype=np.int16).reshape(-1)
        text = self.model.stt(data_array)
        # text = self.model.stt(dataBuff)

        rospy.loginfo(text)

if __name__=="__main__":
    rospy.init_node('ros_nao_audio_service')
    PNAT = ros_nao_deepSpeech()
    rospy.spin()

