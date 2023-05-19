import rospy
from naoqi_bridge_msgs.msg import AudioBuffer
import numpy as np
import wave
import os


""" 
/nao_robot/microphone/naoqi_microphone/audio_raw
/nao_robot/microphone/naoqi_microphone/parameter_descriptions
/nao_robot/microphone/naoqi_microphone/parameter_updates
 """

class ros_nao_audio_recorder():
    def __init__(self):
        rospy.loginfo('subscriber to: /nao_robot/microphone/naoqi_microphone/audio_raw')
        rospy.Subscriber("/nao_robot/microphone/naoqi_microphone/audio_raw",AudioBuffer,callback=self.callback)
        self.audioRawData = []
        rospy.spin()

    def callback(self,data):
        temp = list(data.data)
        self.audioRawData.append(temp)
        # print(len(self.audioRawData),len(self.audioRawData[0]))
        self.int16ToAudio(self.audioRawData)
        # self.getFileSize()


    def int16ToAudio(self,data):
        # specify the parameters for the audio file
        sample_rate = 16000  # samples per second
        num_channels =4  # number of channels (1 for mono, 2 for stereo)
        sample_width = 2  # sample width in bytes (2 for 16-bit)

        # create a new wave file
        # with wave.open('/home/hy/Desktop/audio.wav', 'w') as wav_file:
        #     wav_file.setparams((num_channels, sample_width, sample_rate, 0, 'NONE', 'not compressed'))

        #     # write the data to the file
        #     data = np.array(data, dtype=np.int16)
        #     wav_file.writeframes(data.tostring())
        # wav_file.close()
        #  create a new wave file
        wav_file = wave.open('./audio.wav', 'w')
        wav_file.setparams((num_channels, sample_width, sample_rate, 0, 'NONE', 'not compressed'))

        # write the data to the file
        data = np.array(data, dtype=np.int16)
        wav_file.writeframes(data.tostring())

        # close the file
        wav_file.close()

    def getFileSize(self):
        file_path = "./audio.wav"
        file_size = os.path.getsize(file_path)
        print("Size of the file in bytes:", file_size)


def main():

    rospy.init_node("nao_microphone_sub",anonymous=True)
    rospy.loginfo("start node: nao_microphone_sub")
    audio = ros_nao_audio_recorder()
    rospy.spin()




if __name__=="__main__":

    main()
