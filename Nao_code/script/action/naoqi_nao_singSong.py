from naoqi import ALProxy
import argparse
import time


def main():

    
    # file = audio.loadFile("/home/nao/nao_singing.mp3")
    speech.say("I am not very good singer, but if you want.")
    posture.goToPosture('Stand',0.5)

    id = audio.post.playFile("/home/nao/nao_singing.mp3",1.0,0.0)
    speech.say("^start(animations/Stand/Emotions/Positive/Interested_1)")
    speech.say("^start(BodyTalk/Thinking/Remember_2)")

    posture.goToPosture('Stand',0.5)
    # time.sleep(3)
    speech.say("^start(BodyTalk/Thinking/Remember_2)")
    posture.goToPosture('Stand',0.5)

    audio.wait(id,0)
    speech.say("That's it!")
    speech.say("Do you like it?")
    posture.goToPosture('Stand',0.5)
    led.setIntensity("LeftFaceLedsRed", 1)
    led.setIntensity("RightFaceLedsRed", 1)
    led.setIntensity("LeftFaceLedsGreen", 1)
    led.setIntensity("RightFaceLedsGreen", 1)
    led.setIntensity("LeftFaceLedsBlue", 1)
    led.setIntensity("RightFaceLedsBlue", 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="10.133.242.103",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    speech = ALProxy("ALAnimatedSpeech", args.ip, 9559)
    posture =ALProxy("ALRobotPosture",args.ip, 9559)
    audio = ALProxy("ALAudioPlayer",args.ip, 9559)
    led = ALProxy("ALLeds",args.ip, 9559)
    main()