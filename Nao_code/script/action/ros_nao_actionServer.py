import rospy
from naoqi_bridge_msgs.msg import JointAnglesWithSpeed
import os
import openai
import subprocess
import re


class NaoBot():
    def __init__(self):
        self.pub = rospy.Publisher(
            'joint_angles', JointAnglesWithSpeed, queue_size=10)
        openai.api_key = "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"
        self.chat_history = [{"role": "system",
                              "content": '''You are Nao, helping me with the simulator for robots.
            When I ask you to dance or sing or play guitar, you must only return the functions I gave you, otherwise you must answer 'pass' only.
            You are only allowed to use the functions I have defined for you.
            You are not allowed to use any other hypothetical functions that you think might exist.
            '''}]
        self.chat_history.append({"role": "user",
                                  "content": '''Here are three functions you can only use to command the robot.
naoBot.nao_guitars() - play the guitar.
naoBot.nao_singing() - sing a song or singing.
naoBot.nao_dancing() - dance or dancing.

If I mention dance, answer me: ```python naoBot.nao_dancing()```.
If I mention sing a song or singing, answer me: ```python naoBot.nao_singing()```
If I mention play the guitar or guitar, answer me: ```python naoBot.nao_guitars()```
These are three answers you can only use. If user mentions more than one, only answer one of them.
            '''})
        self.chat_history.append({"role": "user",
                   "content": "I would like to see you dance, let's dance."})
        self.chat_history.append({"role": "assistant",
             "content": """```python naoBot.nao_dancing()```"""})


    def GPT35(self, text):
        openai.api_key = "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"
        self.chat_history.append({"role": "user", "content": text})
        print(self.chat_history)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.chat_history,
            temperature=0.9,
            frequency_penalty=0.1,
            presence_penalty=0.9,
            max_tokens=1000
        )

        return_string = response['choices'][0]['message']['content']

        return return_string

    def nao_guitars(self):
        cmd = 'conda run -n py2 python /home/haoyi/Documents/study/ros_nao/script/action/naoqi_nao_airGuitar.py'
        subprocess.Popen(cmd.split())

    def nao_dancing(self):
        cmd = 'conda run -n py2 python /home/haoyi/Documents/study/ros_nao/script/action/naoqi_nao_dance.py'
        subprocess.Popen(cmd.split())

    def nao_singing(self):
        cmd = 'conda run -n py2 python /home/haoyi/Documents/study/ros_nao/script/action/naoqi_nao_singSong.py'
        subprocess.Popen(cmd.split())


def extract_python_code(content):
    code_block_regex = re.compile(r"```(.*?)```", re.DOTALL)
    code_blocks = code_block_regex.findall(content)
    if code_blocks:
        full_code = "\n".join(code_blocks)

        if full_code.startswith("python"):
            full_code = full_code[7:27]

        return full_code
    else:
        return None


# def interact_function(node):
#     bot = NaoBot(node)
#     while rclpy.ok():
#         user_input = input('user: ')
#         reply = node.send_goal(user_input)
#         code = extract_python_code(reply)
#         if code is not None:
#             try:
#                 exec(code)
#             except Exception as e:
#                 node.send_goal(str(e))


def main():
    rospy.init_node('ros_nao_action', anonymous=True)
    naoBot = NaoBot()
    while True:
        txt = input("user: ")
        res = naoBot.GPT35(txt)
        print(res)
        code = extract_python_code(res)
        if code is not None:
            try:
                exec(code)
            except Exception as e:
                pass



if __name__ == "__main__":
    main()
