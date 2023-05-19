import os 
import openai 
# from pynaoqi_mate import Mate
from std_msgs.msg import String
import rospy

# m = Mate("10.133.242.103", 9559)


def talker():
    rospy.init_node("talker",anonymous=True)
    publisher = rospy.Publisher("openAI",String,queue_size=50)
    rate = rospy.Rate(10)#10 Hz
    openai.api_key = "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"

    while not rospy.is_shutdown():
        text = input("please type: ")
        if text=="exit":
          break
        gpt_prompt = text
        response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=gpt_prompt,
          temperature=0.5,
          max_tokens=400, #4 character is 1 token
          top_p=1.0,
          frequency_penalty=0.5,
          presence_penalty=0.0,
        )
        msg_string = String()
        msg_string.data = response['choices'][0]['text']
        publisher.publish(msg_string)
        rate.sleep()
        rospy.loginfo(response['choices'][0]['text'])


if __name__ == "__main__":
    talker()




