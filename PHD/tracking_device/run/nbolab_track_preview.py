#!/home/nicoluarte/uni/PHD/tracking_device/environments/bg_fg/bin/python3.8
import sys
sys.path.append('../')
from bg_fg import *
import os
import glob
import csv
import socket
import argparse
from configparser import ConfigParser
from time import time as timer

if __name__ == '__main__':
    # read the config file
    parser = ConfigParser()
    parser.read('/home/pi/uni/PHD/tracking_device/config/config.conf')

# read the arguments
parserArg = argparse.ArgumentParser(description='write frame track to csv')
parserArg.add_argument('--file_name', type=str, help='name of the file')
parserArg.add_argument('--background', type=str, help='specify the path of back')
parserArg.add_argument('--capture', type=int, help='set the camera stream vide0 as default')
parserArg.add_argument('--fps', type=int, help='set frames per second for processing')
args = parserArg.parse_args()


# set the background
if args.background is not None:
    bg = cv2.imread(args.background)
    print("loaded background from " + args.background)
    print("background image size: " + str(bg.shape))
else:
    bg = cv2.imread('/home/pi/uni/PHD/tracking_device/background/bg.png')
    print("load default path for background")
    print("background image size: " + str(bg.shape))

# set the capture device
if args.capture is not None:
    cap = cv2.VideoCapture(args.capture)
    _, aux_frame = cap.read()
    print("user defined cam selected: " + str(args.capture))
    print("cam image size: " + str(aux_frame.shape))
else:
    cap = cv2.VideoCapture(0)
    _, aux_frame = cap.read()
    print("default camera selected")
    print("cam image size: " + str(aux_frame.shape))

# set fps control
if args.fps is not None:
    fps = args.fps
    fps /= 1000
    print("user defined FPS: " + str(args.fps))
else:
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps /= 1000
    print("selected camara default FPS:" + str(fps*1000))

while(True):
    # start timer for fps control
    start = timer()
    # read a single frame
    ret, frame = cap.read()
    # process the image
    preview, _, _, points = body_tracking(image_full_process(
        background=bg,
        foreground=frame,
        d=parser.getint('preprocess', 'filter_size'),
        sigma1=parser.getint('preprocess', 'sigma_color'),
        sigma2=parser.getint('preprocess', 'sigma_space'),
        kx=parser.getint('postprocess', 'kernelx'),
        ky=parser.getint('postprocess', 'kernely')
        ))
    # plot stuff
    diff = timer() - start
    img_jpg = cv2.circle(frame, points[0], radius=8, color=(0, 0, 255), thickness=-1)
    img_jpg = cv2.circle(frame, points[1], radius=8, color=(0, 0, 255), thickness=-1)
    img_jpg = cv2.circle(frame, points[2], radius=8, color=(0, 0, 255), thickness=-1)
    cv2.putText(img_jpg, str(diff), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (209, 80, 0, 255), 3)
    cv2.imwrite('/home/pi/uni/PHD/tracking_device/stream/stream.jpg', img_jpg) 
    # end timer for fps control
cap.release()
cv2.destroyAllWindows()
