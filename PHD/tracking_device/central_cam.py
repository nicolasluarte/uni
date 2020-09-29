#!/home/nicoluarte/uni/PHD/tracking_device/environments/bg_fg/bin/python3.8
import cv2
import imagezmq

image_hub = imagezmq.ImageHub()
while True:
    rpi_name, image = image_hub.recv_image()
    cv2.imshow(rpi_name, image)
    cv2.waitKey(1)
    image_hub.send_reply(b'OK')
