#!/home/nicoluarte/uni/PHD/tracking_device/environments/bg_fg/bin/python3.8
import sys
from bg_fg import *
import os
import glob
import csv
import socket
import argparse
from configparser import ConfigParser
from time import time as timer
from os.path import expanduser


if __name__ == '__main__':
    print("HELLO")
    # read the arguments
    parserArg = argparse.ArgumentParser(description='take background picture')
    parserArg.add_argument('-d', '--file_dest', type=str, help='destination of background')
    parserArg.add_argument('-c', '--capture', type=int, help='set the camera stream vide0 as default')
    args = parserArg.parse_args()
    # set defaults or user specified
    # set background folder
    home = expanduser("~")
    hostname = os.popen('hostname').read().rstrip('\n')
    repo = '/uni/PHD/tracking_device/'
    if args.file_dest is not None:
        path = str(args.file_name) + '/bg_' + hostname + '.png'
    else:
        path = str(home) + repo + '/background/bg_' + hostname + '.png'
    # set cam
    if args.capture is not None:
        cap = int(args.capture)
    else:
        cap = 0

    take_background(path, cap)
