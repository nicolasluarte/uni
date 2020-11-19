#!/bin/sh

ffmpeg -re -i "$1" -map 0:v -f v4l2 /dev/"$2"
