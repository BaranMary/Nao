#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Using ALDialog Methods"""

import qi
import argparse
import sys
from naoqi import ALProxy


def main(session):
    """
    Say a text with a local configuration.
    """
    # Get the service ALAnimatedSpeech.

    asr_service = session.service("ALAnimatedSpeech")

    # # set the local configuration
    # configuration = {"bodyLanguageMode":"contextual"}

    # say the text with the local configuration
    asr_service.say("Let's start!")
    asr_service.say('^run(animations/Stand/Waiting/AirGuitar_1)')
    motion.goToPosture('Stand',0.5)
    asr_service.say("Do you like it?")
    motion.goToPosture('Stand',0.5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="10.133.242.103",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    motion = ALProxy("ALRobotPosture", args.ip, 9559)

    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)

