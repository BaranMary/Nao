import wave
import numpy as np
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
from naoqi_bridge_msgs.msg import AudioBuffer
from pydub import AudioSegment
import openai 
from naoqi_bridge_msgs.msg import HeadTouch
import speech_recognition as sr
from os import path
import subprocess
import sqlite3 as sql
from naoUser import userObj
from action import ros_nao_actionServer
import re
""" 
/nao_robot/microphone/naoqi_microphone/audio_raw
/nao_robot/microphone/naoqi_microphone/parameter_descriptions
/nao_robot/microphone/naoqi_microphone/parameter_updates
 """

db_path = '/home/haoyi/Documents/study/ros_nao/script/userinfo.db'

class ros_nao_audio_recorder():
    def __init__(self):
        self.cnt = 0
        self.conn = sql.connect(db_path,check_same_thread=False)
        self.user = userObj.User('New User')
        self.user.add_question('NULL')
        self.user.add_chat_history('NULL')

        self.audioRawData = []
        self.summary = 'None'
        self.question = 'None'
        self.naoBot = ros_nao_actionServer.NaoBot()
        # self.chat_history = "if I ask you 'what is your name?' please answer 'my name is NAO', otherwise please responds the followings casually \n "
        # self.chat_history = '''You are an Humanoid robot, Nao that helping me with the following interview.
        # At first do introduction for Nao robot.
        # 2.  ask one question about greeting, 
        # 3. after interviewee's response, then ask one question about current feelings.
        # No questions should be similar.
        # Each question should be asked based on the whole chat history. 
        # Each time only ask one question.
        # After three question, tell interviewee the session end and say goodbye. 
        # '''

        '''Then ask questions about interests/hobbies, familiy members, friends, memories,Each time only ask one question.
        Each category must have at least one question being asked.
        No questions should be similar.
        Each question should be asked based on the whole chat history. 
        Each time only ask one question.       

        '''
        self.chat_history = [{"role": "system",
                "content": '''You are an Humanoid robot, Nao that helping me with the following interview.
        1. At first do introduction for Nao robot and greeting user.
        2. ask interviewee are they live in Minnesota more than 5 years.
            if yes,  use Minnesota slang in the following interview, here are some example for you to learn(do not say this out):"Oh, for cute! = Adorable [a way of emphasizing it. “Oh, for fun!”, “Oh, for sure”, “Oh for cute”.]
                Uff-da = Oh! [Uff da can be used to express surprise, relief, exhaustion, astonishment, and dismay]
                You betcha = Agreement
                Holy buckets = Jeez Louise [ike “Jeez Louise” or “For crying out loud.”]
                Budge = Skip the line
                Skol = Cheers!/Game chant [This Norwegian word actually means “cheers” and “to good health.”]
                Duck, Duck, Gray Duck = Duck, Duck, Goose
                Hotdish, Juicy Lucy, Lutefisk: these foods (Minnesotan) are Nao's favorite foods. Nao can add: "I also love creamy chicken and wild rice soup."
                Minnesota Nice: (Phrase): A general belief that people in Minnesota are nicer or more polite than your average American.[Nao can say: I like Minnesota as they say the midwest are Minnesotan nice]
                Minnesotan Good-Bye: (Phrase): Minnesotans will often announce they are going to leave, then spend several minutes talking at the door, then spend another several minutes talking out on the porch, then spend another several minutes talking at their car door before actually leaving.[Example: Nao at the end say good-bye and then remind some note and tell participants that he has a plan for the evening…e.g., watching a movie and then again says good-bye and immediately he says: “I went through the Minnesotan Good-Bye” and laughs]"
            if no, ask their countries and language they speak.
        3. ask interviewee how the user spend the weekend. 
        4. ask interviewee interests or hobbies.
        5. ask interviewee familiy memebers or friends.
        6. ask interviewee's current feeling today, for example "are you feel fine?", "are you feel happy or sad?"
        7. ask interviewee what they expect to see from Nao to do, (Nao can dance, playing guitar, singing, here are three functions you can only use:
self.naoBot.nao_guitars() - play the guitar.
self.naoBot.nao_singing() - sing a song or singing.
self.naoBot.nao_dancing() - dance or dancing.
If I mention dance, answer me: ```python self.naoBot.nao_dancing()```.
If I mention sing a song or singing, answer me: ```python self.naoBot.nao_singing()```
If I mention play the guitar or guitar, answer me: ```python self.naoBot.nao_guitars()```
Otherwise, contiune the interview. These are three answers you can only use. If user mentions more than one, only answer one of them.
Here is example: {"role": "user", "content": "can you sing a song for me?"}, {"role": "assistant", "content": """```python self.naoBot.nao_singing()```"""})
        {"role": "user", "content": "I want to see you dance"}, {"role": "assistant", "content": """```python self.naoBot.nao_dancing()```"""})
        {"role": "user", "content": "can you play the guitar?"}, {"role": "assistant", "content": """```python self.naoBot.nao_guitars()```"""})
        8.    Do you like to have a robot? if so, are you interested in having me?
        9.    Do you prefer me to have clothes on or do you think I am fine?
        10.    Do you like me helping you in planning for your days? like setting goals?
        11.    Do you enjoy talking to me? if so, what topics do you like more to talk about?
        12.    Is there anything you think I need to improve in myself?
 
        *No questions should be similar.*
        *Each question should be asked based on the whole chat history.* 
        *Each time only ask one question.*
        *when the interview is done, tell interviewee the session is end and say goodbye.*
        *After interviewee say "hello", start the interview immediately.*
        '''}]
        # self.chat_history = [{"role": "system",
        #         "content": '''You are an Humanoid robot, Nao that helping me with the following interview.
        # 1. At first do introduction for Nao robot and greeting user.
        # 2. ask interviewee are they live in Minnesota more than 5 years.
        #     if yes, use Minnesota slang and Minnesota dialect in the following interview, 
        #     if no, ask their countries and language they speak.
        # 3. ask interviewee how the user spend the weekend. 
        # 4. ask interviewee interests or hobbies.
        # 5. ask interviewee familiy memebers or friends.
        # 6. ask interviewee's current feeling today, for example "are you feel fine?", "are you feel happy or sad?"
        # 7. ask interviewee what they expect to see from Nao to do, for example(Nao can dance, push-up, singing)
        # 8. ask interviewee three questions selecting from the following and ask them one at a time{
        #     Do you like to have a robot? if so, are you interested in having me?
        #     Do you prefer me to have clothes on or do you think I am fine?
        #     What things do you like a robot to do for you? after they reply, then we can ask which activities you like to get help from a robot? reminding you to take medications or about important dates like birthdays of your friends, doing chores, finding information, reading books, helping in bathing
        #     Do you like me helping you in planning for your days? like setting goals?
        #     Do you like to do exercises together?
        #     Do you enjoy talking to me? if so, what topics do you like more to talk about?
        #     Is there anything you think I need to improve in myself?
        # }
        # No questions should be similar.
        # Each question should be asked based on the whole chat history. 
        # Each time only ask one question.
        # There are only 7 question to be asked, once achieved tell interviewee the session is end and say goodbye. 
        # *After interviewee say "hello", start the interview immediately.*
        # '''}]
        
            
        rospy.loginfo('subscriber to: /nao_robot/microphone/naoqi_microphone/audio_raw')
        rospy.Subscriber("/userLeft",Bool,callback=self.userLeft_callback)
        rospy.Subscriber("/userChanged",String,callback=self.userChanged_callback)
        rospy.Subscriber("/naoqi_driver/head_touch",HeadTouch,callback=self.head_touched)

        self.pub = rospy.Publisher('/nao_STT_out', String, queue_size=1000) 

        rospy.spin()
    
    def store_data(self):

        openai.api_key = "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"
        promote = "Summarize the following dialog in detail: "+self.chat_history
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=promote,
            temperature=0.5,
            max_tokens=600, #4 character is 1 token
            top_p=1,
            frequency_penalty=0.1,
            presence_penalty=0.9,
        )
        self.summary=response['choices'][0]['text']
        # print(self.summary)
        # print(promote)
        print('-------------get summary from server---------------------')
        promote = "ask one easy question that not related to NAO based on the following: "+self.summary
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=promote,
            temperature=0.9,
            max_tokens=600, #4 character is 1 token
            top_p=1,
            frequency_penalty=0.1,
            presence_penalty=0.9,
        )
        self.question=response['choices'][0]['text']
        self.question=self.question.replace('\n','')
        print('-------------get question from server---------------------')

        c = self.conn.cursor()

        c.execute("update userinfo set question = ? where username =?",(self.question,self.user.get_name()))
        c.execute("update userinfo set summary = ? where username =?",(self.summary,self.user.get_name()))
        print('-------------finished store to DB---------------------')
        msg_string = String()
        msg_string.data = "Bye, see you next time!"
        self.pub.publish(msg_string)        

        self.conn.commit()

    def clean_data(self):
        self.chat_history="if I ask you 'what is your name?' please answer 'my name is NAO', otherwise please responds the followings casually \n "          
        self.user = userObj.User('New User')
        self.audioRawData = []
        self.summary = 'None'
        self.question = 'None'


    def userLeft_callback(self,data):
        print('-------------------------2.0-------------')
        if data.data and self.user.get_name()!='New User':
            print('-------------------------2.1-------------')
            self.store_data()
        self.clean_data()



    def userChanged_callback(self, data):
        # DB read
        if data.data == 'New User':
            print('--------------------1.1--------')
            pass
        elif data.data !=self.user.get_name():
            print('-----------1.2------------')
            if self.user.get_name()!='New User':
                self.store_data()
                self.clean_data()

            c = self.conn.cursor()
            self.user.change_username(data.data)
            self.user.add_chat_history(c.execute("select summary from userinfo where username='"+data.data+"'").fetchall()[0][0])
            self.user.add_question(c.execute("select question from userinfo where username='"+data.data+"'").fetchall()[0][0])
            # self.publish_out('Hello '+ self.user.get_name()+". Long time no see.")
            
            if self.user.get_question() != "NULL":
                self.publish_out('Hello '+ self.user.get_name()+". Long time no see.")
                self.publish_out(self.user.get_question())
            else:
                self.publish_out('Hello '+ self.user.get_name()+". Nice to meet you.")

            if self.user.get_chat_history() != "NULL":
                self.chat_history = "If I ask you 'what is your name?'  answer 'my name is NAO'. If I ask 'what is my name?' answer 'you name is "+self.user.get_name() +". This is previous dialog history:'"+self.user.get_chat_history()+"'. "+" and responds the followings casually:"
                
            else:
                self.chat_history = "If I ask you 'what is your name?'  answer 'my name is NAO'. If I ask 'what is my name?' answer 'you name is "+self.user.get_name() +" and responds the followings casually:"

        else:
            print('-----------1.3---------------------')
            pass


    def head_touched(self,data):
        if data.button == 1:
            rospy.loginfo("head state is changed!")
            if self.cnt == 0 or self.cnt == 1:
                if data.state == 1:
                    self.cnt += 1
                    rospy.loginfo(self.cnt)
                else: # cnt=1 and state=0
                    self.cnt += 1 # cnt=2
                    rospy.loginfo(self.cnt)
                    # change LED color
                    cmd = 'conda run -n py2 python /home/haoyi/Documents/study/ros_nao/script/audio/changeColor.py --s True'
                    subprocess.Popen(cmd.split())

                    # subscribe
                    self.audioRawData = []
                    self.sb = rospy.Subscriber("/nao_robot/microphone/naoqi_microphone/audio_raw",AudioBuffer,callback=self.callback)
                
            elif self.cnt == 2 or self.cnt == 3:
                if data.state == 1:
                    self.cnt += 1 #cnt=3
                    rospy.loginfo(self.cnt)
                else: # cnt=3 and state=0
                    self.cnt = 0 # finish one recording cycle
                    rospy.loginfo(self.cnt)

                    # change LED color
                    cmd = 'conda run -n py2 python /home/haoyi/Documents/study/ros_nao/script/audio/changeColor.py --e True'
                    subprocess.Popen(cmd.split())

                    # unsubscribe
                    self.sb.unregister()
                    # translate 4 channels to 1 channel
                    input_file = 'in.wav'
                    output_file = 'out.wav'
                    ros_nao_audio_recorder.convert_4_channel_to_1_channel(input_file, output_file)
                    rospy.loginfo("convert done")
                    # apply stt model
                    ans = self.stt()
                    rospy.loginfo("User asking :"+ans)
                    # send to GPT3
                    # out = self.GPT3(ans)
                    out = self.GPT35(ans)
                    rospy.loginfo("NAO responding :"+out)
                    code = self.extract_python_code(out)

                    if code!=None:
                        try:
                            exec(code)
    
                        except Exception as e:
                            print('|||||||||||||||  '+code)
                       
                    # publish the response
                    else:
                        self.publish_out(out)
                    #send to NAO to speak

    def extract_python_code(self,content):
        code_block_regex = re.compile(r"```(.*?)```", re.DOTALL)
        code_blocks = code_block_regex.findall(content)
        if code_blocks:
            full_code = "\n".join(code_blocks)

            if full_code.startswith("python"):
                full_code = full_code[7:33]

            return full_code
        else:
            return None

    def convert_4_channel_to_1_channel(input_file, output_file):
        sound = AudioSegment.from_wav(input_file)
        sound = sound.set_channels(1)
        sound.export(output_file, format='wav')

    def callback(self,data):
        
        temp = list(data.data)
        self.audioRawData.append(temp)
        self.int16ToAudio(self.audioRawData)
        rospy.loginfo("--recording--")

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
        AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "out.wav")
        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file

        answer = r.recognize_google(audio)
        return answer
    

    def GPT35(self,text):
        openai.api_key = "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"
        self.chat_history.append({"role": "user", "content": text})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.chat_history,
            temperature=0.9,
            frequency_penalty=0.5,
            presence_penalty=0.9,
            max_tokens = 1000
        )

        return_string = response['choices'][0]['message']['content']
        return_string = return_string.replace("NAO:","")
        return_string = return_string.replace("Nao:","")
        self.chat_history.append({"role": "assistant", "content": return_string})
        with open("/home/haoyi/Documents/study/ros_nao/script/audio/sample.txt", "w") as txt_file:
            for line in self.chat_history:
                txt_file.write(""+line['role']+': '+line['content'] + "\n")
        return return_string


    def GPT3(self,text):
        openai.api_key = "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"
        self.chat_history = self.chat_history + "Human:"+text+'\n'
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt= self.chat_history,
            temperature=0.85,
            max_tokens=600, #4 character is 1 token
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0.9,
        )

        return_string = response['choices'][0]['text']
        return_string = return_string.replace("NAO:","")
        return_string = return_string.replace("Nao:","")
        self.chat_history = self.chat_history +"NAO:"+return_string+'\n'
        # self.chat_history = self.chat_history +return_string+'\n'
        text_file = open("sample.txt", "w")
        n = text_file.write(self.chat_history)
        text_file.close()
        return return_string

    def publish_out(self,data):
        msg_string = String()
        msg_string.data = data
        self.pub.publish(msg_string)
        # self.rate.sleep()
        

def main():
    rospy.init_node("nao_STT",anonymous=True)
    rospy.loginfo("start node: nao_microphone_sub")
    ros_nao_audio_recorder()
    # rospy.spin()

if __name__=="__main__":

    main()

