#!/home/nicoluarte/uni/PHD/tracking_device/environments/bg_fg/bin/python3.8
import cv2
import imagezmq
from bg_fg import *


bg = cv2.imread('/home/nicoluarte/uni/PHD/tracking_device/background.png')
image_hub = imagezmq.ImageHub()
while True:
    rpi_name, image = image_hub.recv_image()
    _, _, _, points = body_tracking(image_full_process(bg, image))
    print(points)
    cv2.imshow(rpi_name, image)
    cv2.waitKey(1)
    image_hub.send_reply(b'OK')


