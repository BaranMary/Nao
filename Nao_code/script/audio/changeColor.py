from pynaoqi_mate import Mate
import argparse

ip = '10.133.242.103'

parser = argparse.ArgumentParser(
                    prog = 'changeColor',
                    description = 'change NAO eye led color',
                    epilog = 'Text at the bottom of help')

parser.add_argument('--s',default=False)     
parser.add_argument('--e',default=False)

args = parser.parse_args()

if args.s=="True":
    # print("s equals true now")
    Mate(ip, 9559).ALLeds.setIntensity("LeftFaceLedsRed", 0.1)
    Mate(ip, 9559).ALLeds.setIntensity("RightFaceLedsRed", 0.1)
    
if args.e=="True":
    # print("e equals true now")
    Mate(ip, 9559).ALLeds.setIntensity("LeftFaceLedsRed", 1)
    Mate(ip, 9559).ALLeds.setIntensity("RightFaceLedsRed", 1)

