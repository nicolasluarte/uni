import socket
import time
from imutils.video import videoStream
import imagezqm

sender = imagezmq.ImageSender(connect_to='192.168.1.100:5555')

rpi_name = socket.gethostname()
picam = VideoStream(0).start()
time.sleep(2.0)
while True:
    image = picam.read()
    sender.send_image(rpi_name, image)
