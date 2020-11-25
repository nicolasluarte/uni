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
    parser.read('../config/config.conf')

# read the arguments
parserArg = argparse.ArgumentParser(description='write frame track to csv')
parserArg.add_argument('--file_name', type=str, help='name of the file')
parserArg.add_argument('--background', type=str, help='specify the path of back')
parserArg.add_argument('--capture', type=int, help='set the camera stream vide0 as default')
parserArg.add_argument('--fps', type=int, help='set frames per second for processing')
args = parserArg.parse_args()


# read from virtual camera and write to csv

# csv label, so every record is distinct
if args.file_name is not None:
    label = str(args.file_name)
else:
    label = str(socket.gethostname()) + "_" + \
        datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

# set the background
if args.background is not None:
    bg = cv2.imread(args.background)
    print("loaded background from " + args.background)
else:
    bg = cv2.imread('../background/bg.png')
    print("load default path for background")

# set the capture device
if args.capture is not None:
    cap = cv2.VideoCapture(args.capture)
    print("user defined cam selected: " + str(args.capture))
else:
    cap = cv2.VideoCapture(0)
    print("default camera selected")

# set fps control
if args.fps is not None:
    fps = args.fps
    fps /= 1000
    print("user defined FPS: " + str(args.fps))
else:
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps /= 1000
    print("selected camara default FPS:" + str(fps*1000))

# start writing into csv
with open('../csv_bak/' + label + '.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["YEAR", "MONTH", "DAY", "HOUR", "MINUTE", "SECOND", "MICROSECOND", "body_x", "body_y", "tail_x", "tail_y", "head_x", "head_y"])
    while(True):
        # start timer for fps control
        start = timer()
        # read a single frame
        ret, frame = cap.read()
        # process the image
        fp, _, _, points = body_tracking(image_full_process(
            background=bg,
            foreground=frame,
            d=parser.getint('preprocess', 'filter_size'),
            sigma1=parser.getint('preprocess', 'sigma_color'),
            sigma2=parser.getint('preprocess', 'sigma_space'),
            kx=parser.getint('postprocess', 'kernelx'),
            ky=parser.getint('postprocess', 'kernely')
            ))
        time_stamp = datetime.datetime.now().strftime("%Y %m %d %H %M %S %f")
        log = list(map(int, time_stamp.split())) + [item for i in points for item in i]
        writer.writerow(log)
        # end timer for fps control
        diff = timer() - start
        while diff < fps:
            diff = timer() - start
cap.release()
cv2.destroyAllWindows()
