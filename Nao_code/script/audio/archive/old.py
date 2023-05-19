from deepspeech import Model
import argparse
import wave
import numpy as np
import rospy
from std_msgs.msg import String
from naoqi_bridge_msgs.msg import AudioBuffer
import time
from pydub import AudioSegment
import openai 
from std_msgs.msg import String

""" 
/nao_robot/microphone/naoqi_microphone/audio_raw
/nao_robot/microphone/naoqi_microphone/parameter_descriptions
/nao_robot/microphone/naoqi_microphone/parameter_updates
 """

TIME_TO_RECORD = 5
end = int(time.time()) + TIME_TO_RECORD
STT_model_PATH='./pretrained_model/deepspeech-0.9.3-models.pbmm'

class ros_nao_audio_recorder():
    def __init__(self):
        rospy.loginfo('subscriber to: /nao_robot/microphone/naoqi_microphone/audio_raw')
        self.sb = rospy.Subscriber("/nao_robot/microphone/naoqi_microphone/audio_raw",AudioBuffer,callback=self.callback)
        self.audioRawData = []
        self.rate = rospy.Rate(10)#10 Hz
        self.pub = rospy.Publisher('/nao_STT_out', String, queue_size=1000)       
        rospy.spin()
        
    def convert_4_channel_to_1_channel(input_file, output_file):
        sound = AudioSegment.from_wav(input_file)
        sound = sound.set_channels(1)
        sound.export(output_file, format='wav')   

    def callback(self,data):
        if int(time.time()) >= end:
            print("ending at %d" % int(time.time()))
            self.sb.unregister()
            input_file = 'in.wav'
            output_file = 'out.wav'
            ros_nao_audio_recorder.convert_4_channel_to_1_channel(input_file, output_file)
            rospy.loginfo("record done")
            ans = self.stt()
            rospy.loginfo("User asking :"+ans)
            out = self.GPT3(ans)
            rospy.loginfo("NAO responding :"+out)
            self.publish_out(out)


        temp = list(data.data)
        self.audioRawData.append(temp)
        self.int16ToAudio(self.audioRawData)
        rospy.loginfo("callback end")

    def int16ToAudio(self,data):
        
        # specify the parameters for the audio file
        sample_rate = 16000  # samples per second
        num_channels = 4 # number of channels (1 for mono, 2 for stereo)
        sample_width = 2  # sample width in bytes (2 for 16-bit)
        
        #  create a new wave file
        wav_file = wave.open('./in.wav', 'wb')
        wav_file.setparams((num_channels, sample_width, sample_rate, 0, 'NONE', 'not compressed'))

        # write the data to the file
        data = np.array(data, dtype=np.int16)
        wav_file.writeframes(data.tobytes())

        # close the file
        wav_file.close()
    def stt(self):
        ds = Model(STT_model_PATH)
        desired_sample_rate = ds.sampleRate()
        fin = wave.open('./out.wav', 'rb')
        fs_orig = fin.getframerate()
        if fs_orig != desired_sample_rate:
            print('Warning: original sample rate ({}) is different than {}hz. Resampling might produce erratic speech recognition.'.format(fs_orig, desired_sample_rate), file=sys.stderr)
            # fs_new, audio = convert_samplerate(args.audio, desired_sample_rate)
        else:
            audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)

        audio_length = fin.getnframes() * (1/fs_orig)
        fin.close()
        answer = ds.stt(audio)
        return answer
    def GPT3(self,text):
        openai.api_key = "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"
        gpt_prompt = "please respond casually: "+text
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=gpt_prompt,
            temperature=0.5,
            max_tokens=400, #4 character is 1 token
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
        return  response['choices'][0]['text']

    def publish_out(self,data):
        msg_string = String()
        msg_string.data = data
        self.pub.publish(msg_string)
        self.rate.sleep()
        

def main():

    rospy.init_node("nao_STT",anonymous=True)
    rospy.loginfo("start node: nao_microphone_sub")
    audio = ros_nao_audio_recorder()
    rospy.spin()

if __name__=="__main__":

    main()


