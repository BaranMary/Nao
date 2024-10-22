# Choregraphe simplified export in Python.
from naoqi import ALProxy
import qi
import argparse
import sys

names = list()

times = list()

keys = list()


names.append("HeadPitch")

times.append([1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56,
             8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.8])

keys.append([-0.476475, 0.338594, -0.476475, 0.338594, -0.476475, 0.338594, -0.476475, 0.338594, -
            0.476475, 0.338594, -0.476475, 0.338594, -0.476475, 0.338594, -0.476475, 0.338594, -0.17185])


names.append("HeadYaw")

times.append([1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56,
             8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.8])

keys.append([-0.745256, 0.289725, -0.745256, 0.289725, -0.745256, 0.289725, -0.745256, 0.289725,
            0.745256, -0.289725, 0.745256, -0.289725, 0.745256, -0.289725, 0.745256, -0.289725, 0.00916195])


names.append("LAnklePitch")

times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48,
             8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])

keys.append([-0.046062, 0.0444441, 0.161028, 0.0444441, 0.161028, 0.0444441, 0.161028, 0.0444441,
            0.161028, 0.092082, 0.082878, 0.092082, 0.082878, 0.092082, 0.082878, 0.092082, 0.082878, 0.0873961])


names.append("LAnkleRoll")

times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48,
             8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])

keys.append([-0.0183661, 0.062936, -0.248467, 0.062936, -0.248467, 0.062936, -0.248467, 0.062936, -
            0.248467, -0.26389, 0.0904641, -0.26389, 0.0904641, -0.26389, 0.0904641, -0.26389, 0.0904641, -0.121144])


names.append("LElbowRoll")

times.append([0.8, 1.24, 1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56, 8.12, 8.72, 9.12, 9.52,
             10, 10.44, 10.84, 11.24, 11.72, 12.08, 12.48, 12.88, 13.36, 13.76, 14.16, 14.56, 15.04, 15.88])

keys.append([-1.37289, -1.12923, -0.369652, -0.202446, -0.369652, -0.202446, -0.369652, -0.202446, -0.369652, -0.202446, -1.54462, -0.138102, -1.309, -
            0.257754, -1.4591, -0.138102, -1.309, -0.257754, -1.4591, -0.138102, -1.309, -0.257754, -1.4591, -0.138102, -1.309, -0.257754, -1.4591, -0.424876])


names.append("LElbowYaw")

times.append([0.8, 1.24, 1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56, 8.12, 8.72, 9.12, 9.52,
             10, 10.44, 10.84, 11.24, 11.72, 12.08, 12.48, 12.88, 13.36, 13.76, 14.16, 14.56, 15.04, 15.88])

keys.append([-0.65506, -1.76453, -0.380475, -0.618244, -0.380475, -0.618244, -0.380475, -0.618244, -0.380475, -0.618244, -1.65632, 0.851412, 0.0750492, 0.00157596,
            0.460767, 0.851412, 0.0750492, 0.00157596, 0.460767, 0.851412, 0.0750492, 0.00157596, 0.460767, 0.851412, 0.0750492, 0.00157596, -0.682424, -1.21037])


names.append("LHand")

times.append([0.8, 1.24, 1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56, 8.12, 8.72, 9.12, 9.52,
             10, 10.44, 10.84, 11.24, 11.72, 12.08, 12.48, 12.88, 13.36, 13.76, 14.16, 14.56, 15.04, 15.88])

keys.append([0.2, 0.6, 0.2648, 0.264, 0.2648, 0.264, 0.2648, 0.264, 0.2648, 0.264, 0.13, 0.678, 0.3,
            0.6784, 0.3, 0.678, 0.3, 0.6784, 0.3, 0.678, 0.3, 0.6784, 0.3, 0.678, 0.3, 0.6784, 0.3, 0.2968])


names.append("LHipPitch")

times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48,
             8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])

keys.append([-0.153358, 0.185656, 0.147306, 0.185656, 0.147306, 0.185656, 0.147306, 0.185656, 0.147306,
            0.101202, 0.259204, 0.101202, 0.259204, 0.101202, 0.259204, 0.101202, 0.259204, 0.139636])


names.append("LHipRoll")

times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48,
             8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])

keys.append([0.00464395, -0.144154, 0.329852, -0.144154, 0.329852, -0.144154, 0.329852, -0.144154,
            0.329852, 0.297554, -0.14117, 0.297554, -0.14117, 0.297554, -0.14117, 0.297554, -0.14117, 0.10282])


names.append("LHipYawPitch")

times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48,
             8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])

keys.append([-0.443284, -0.37272, -0.357381, -0.37272, -0.357381, -0.37272, -0.357381, -0.37272, -
            0.357381, -0.37272, -0.357381, -0.37272, -0.357381, -0.37272, -0.357381, -0.37272, -0.357381, -0.170232])


names.append("LKneePitch")

times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48,
             8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])

keys.append([0.404934, -0.090548, -0.0798099, -0.090548, -0.0798099, -0.090548, -0.0798099, -0.090548, -0.0798099, -
            0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0782759])


names.append("LShoulderPitch")

times.append([0.8, 1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56, 8.12,
             8.72, 9.52, 10.44, 11.24, 12.08, 12.88, 13.76, 14.56, 15.36, 15.88])

keys.append([0.639635, 1.74718, 1.85611, 1.74718, 1.85611, 1.74718, 1.85611, 1.74718, 1.85611, 1.21475, -
            1.19188, 0.995607, -1.19188, 0.995607, -1.19188, 0.995607, -1.19188, 0.995607, 1.06465, 1.47106])


names.append("LShoulderRoll")

times.append([0.8, 1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76, 7.56, 8.12, 8.72, 9.12, 9.52, 10,
             10.44, 10.84, 11.24, 11.72, 12.08, 12.48, 12.88, 13.36, 13.76, 14.16, 14.56, 15.04, 15.88])

keys.append([0.340507, 0.24233, 0.196309, 0.24233, 0.196309, 0.24233, 0.196309, 0.24233, 0.196309, 0.165806, 0.328317, 0.595157, -0.314159,
            0.595157, 0.328317, 0.595157, -0.314159, 0.595157, 0.328317, 0.595157, -0.314159, 0.595157, 0.328317, 0.595157, -0.314159, 0.595157, 0.153358])


names.append("LWristYaw")

times.append([0.8, 1.24, 1.64, 2.44, 3.36, 4.16, 5.04, 5.84, 6.76,
             7.56, 8.72, 9.52, 10.44, 11.24, 12.08, 12.88, 13.76, 14.56, 15.88])

keys.append([0.11961, -1.45037, -0.395814, -0.420357, -0.395814, -0.420357, -0.395814, -0.420357, -0.395814, -
            0.420357, -0.107338, -0.400331, -0.107338, -0.400331, -0.107338, -0.400331, -0.107338, -0.400331, 0.0827939])


names.append("RAnklePitch")

times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48,
             8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])

keys.append([-0.052114, 0.092082, 0.082878, 0.092082, 0.082878, 0.092082, 0.082878, 0.092082, 0.082878,
            0.0444441, 0.161028, 0.0444441, 0.161028, 0.0444441, 0.161028, 0.0444441, 0.161028, 0.093616])


names.append("RAnkleRoll")

times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48,
             8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])

keys.append([0.0966839, 0.26389, -0.0904641, 0.26389, -0.0904641, 0.26389, -0.0904641, 0.26389, -
            0.0904641, -0.062936, 0.248467, -0.062936, 0.248467, -0.062936, 0.248467, -0.062936, 0.248467, 0.119694])


names.append("RElbowRoll")

times.append([0.88, 1.32, 1.72, 2.12, 2.52, 3, 3.44, 3.84, 4.24, 4.72, 5.12, 5.52, 5.92, 6.4,
             6.84, 7.24, 7.64, 8.12, 8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.08, 15.4, 15.8])

keys.append([1.34689, 1.1205, 0.138102, 1.309, 0.257754, 1.4591, 0.138102, 1.309, 0.257754, 1.4591, 0.138102, 1.309, 0.257754, 1.4591, 0.138102,
            1.309, 0.257754, 1.54462, 0.369652, 0.202446, 0.369652, 0.202446, 0.369652, 0.202446, 0.369652, 0.202446, 0.82205, 0.886627, 0.429562])


names.append("RElbowYaw")

times.append([0.88, 1.32, 1.72, 2.12, 2.52, 3, 3.44, 3.84, 4.24, 4.72, 5.12, 5.52, 5.92, 6.4,
             6.84, 7.24, 7.64, 8.12, 8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.08, 15.4, 15.8])

keys.append([0.59515, 0.567232, -0.851412, -0.0750492, -0.00157596, -0.460767, -0.851412, -0.0750492, -0.00157596, -0.460767, -0.851412, -0.0750492, -0.00157596, -
            0.460767, -0.851412, -0.0750492, -0.00157596, 1.65632, 0.380475, 0.618244, 0.380475, 0.618244, 0.380475, 0.618244, 0.380475, 0.618244, 1.57952, 1.03323, 1.21028])


names.append("RHand")

times.append([0.88, 1.32, 1.72, 2.12, 2.52, 3, 3.44, 3.84, 4.24, 4.72, 5.12, 5.52, 5.92, 6.4,
             6.84, 7.24, 7.64, 8.12, 8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.4, 15.8])

keys.append([0.2, 0.5, 0.678, 0.3, 0.6784, 0.3, 0.678, 0.3, 0.6784, 0.3, 0.678, 0.3, 0.6784, 0.3,
            0.678, 0.3, 0.6784, 0.13, 0.2648, 0.264, 0.2648, 0.264, 0.2648, 0.264, 0.2648, 0.264, 0.24, 0.2976])


names.append("RHipPitch")

times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48,
             8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])

keys.append([-0.177985, 0.101202, 0.259204, 0.101202, 0.259204, 0.101202, 0.259204, 0.101202, 0.259204,
            0.185656, 0.147306, 0.185656, 0.147306, 0.185656, 0.147306, 0.185656, 0.147306, 0.131882])


names.append("RHipRoll")

times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48,
             8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])

keys.append([-0.11961, -0.297554, 0.14117, -0.297554, 0.14117, -0.297554, 0.14117, -0.297554, 0.14117,
            0.144154, -0.329852, 0.144154, -0.329852, 0.144154, -0.329852, 0.144154, -0.329852, -0.0966001])


names.append("RHipYawPitch")

times.append([1.56, 3.28, 4.96, 6.68, 8.56, 10.28, 11.92, 13.6, 15.72])

keys.append([-0.37272, -0.37272, -0.37272, -0.37272, -
            0.37272, -0.37272, -0.37272, -0.37272, -0.170232])


names.append("RKneePitch")

times.append([0.68, 1.56, 2.36, 3.28, 4.08, 4.96, 5.76, 6.68, 7.48,
             8.56, 9.36, 10.28, 11.08, 11.92, 12.72, 13.6, 14.4, 15.72])

keys.append([0.426494, -0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0904641, -
            0.0904641, -0.090548, -0.0798099, -0.090548, -0.0798099, -0.090548, -0.0798099, -0.090548, -0.0798099, -0.091998])


names.append("RShoulderPitch")

times.append([0.88, 1.72, 2.52, 3.44, 4.24, 5.12, 5.92, 6.84, 7.64,
             8.12, 8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.4, 15.8])

keys.append([0.915841, -1.19188, 0.995607, -1.19188, 0.995607, -1.19188, 0.995607, -1.19188, 0.995607,
            1.21475, 1.74718, 1.85611, 1.74718, 1.85611, 1.74718, 1.85611, 1.74718, 1.85611, 1.18508, 1.47268])


names.append("RShoulderRoll")

times.append([0.88, 1.32, 1.72, 2.12, 2.52, 3, 3.44, 3.84, 4.24, 4.72, 5.12, 5.52, 5.92, 6.4,
             6.84, 7.24, 7.64, 8.12, 8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.08, 15.8])

keys.append([-0.266959, -0.670206, -0.328317, -0.595157, 0.314159, -0.595157, -0.328317, -0.595157, 0.314159, -0.595157, -0.328317, -0.595157, 0.314159, -
            0.595157, -0.328317, -0.595157, 0.314159, -0.165806, -0.24233, -0.196309, -0.24233, -0.196309, -0.24233, -0.196309, -0.24233, -0.196309, -0.455531, -0.16418])


names.append("RWristYaw")

times.append([0.88, 1.32, 1.72, 2.52, 3.44, 4.24, 5.12, 5.92, 6.84,
             7.64, 8.64, 9.44, 10.36, 11.16, 12, 12.8, 13.68, 14.48, 15.8])

keys.append([-0.401949, 1.39277, 0.107338, 0.400331, 0.107338, 0.400331, 0.107338, 0.400331, 0.107338,
            0.400331, 0.395814, 0.420357, 0.395814, 0.420357, 0.395814, 0.420357, 0.395814, 0.420357, 0.108872])



def main(session):
    asr_service = session.service("ALAnimatedSpeech")

    asr_service.say("Let's Dance!")
    audio.post.playFileFromPosition("/home/nao/a.mp3",29.0,0.8,0.0)

    posture.goToPosture('Crouch',0.5)
    motion.angleInterpolation(names, keys, times, True)
    audio.stopAll()
    asr_service.say("Do you like it?")
    posture.goToPosture('Stand',0.5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="10.133.242.103",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    motion = ALProxy("ALMotion", args.ip, 9559)
    posture =ALProxy("ALRobotPosture",args.ip, 9559)
    audio = ALProxy("ALAudioPlayer",args.ip, 9559)

    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)