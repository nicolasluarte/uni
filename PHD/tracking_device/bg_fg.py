#!/home/nicoluarte/uni/PHD/tracking_device/environments/bg_fg/bin/python3.8
import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import skfmm
import paramiko

""" bilateral filter preserver sharp edges, and smoothes each pixel as a weighted average of intensity values from nerby pixels; this process is used for denoising the image; function returns a gray image with bilateral filtering """
def preprocess_image(image):
    bl_filter_image = cv2.bilateralFilter(image, 7, 150, 150) # test out parameters
    gray_image = cv2.cvtColor(bl_filter_image, cv2.COLOR_BGR2GRAY)
    return gray_image

""" the image gets dilated (if one pixel under the kernel is '1' the a determined pixel is also '1') and then followed by erosion (a pixel is 1 if all pixels under the kernel are 1) """
def postprocess_image(image):
   kernel = np.ones((15,15), np.uint8) 
   close_operation = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
   _, thresholded = cv2.threshold(close_operation, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
   blur = cv2.medianBlur(thresholded, 5)
   return blur

""" takes the bigger contour area, all small areas are considered noise as there's is to be only one animal; it also requires a gray image"""
def contour_extraction(image):
    ret, thresh = cv2.threshold(image, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    extraction = cv2.drawContours(np.zeros((image.shape[0], image.shape[1])), [max(contours, key = cv2.contourArea)], -1, 255, thickness=-1)
    return extraction


""" outputs the difference between the background and background + animal, so animal can be isolated """
def bgfg_diff(background, foreground):
    bg = preprocess_image(background)
    fg = preprocess_image(foreground)
    diff = cv2.absdiff(bg, fg)
    return diff

""" this function does all the pipeline """
def image_full_process(background, foreground):
    # convert rgb to gray scale
    diff = bgfg_diff(foreground, background)
    # post process the difference to remove noise
    diff_postproc = postprocess_image(diff)
    # extract the biggest contour area and paste it in an empty canvas
    final_image = contour_extraction(diff_postproc)
    return final_image

""" function to get the head, tail and body position
    requires the final_image"""
def body_tracking(image):
    # first we get the geodesic distance
    # because mice and rats are fluffy the torso is the furthest away distance
    distance = skfmm.distance(image)
    # get the highest point
    bx, by = np.unravel_index(distance.argmax(), distance.shape)
    # the furthest away point from this is the tail
    # create a boolen mask
    mask = ~image.astype(bool)
    # we mark with 0 the body
    tail = np.ones_like(image)
    tail[bx][by] = 0
    t = np.ma.MaskedArray(tail, mask)
    # get the distance from 0
    # the highest one is the tip of the tail
    tail_distance = skfmm.distance(t)
    # same to get the head, but calculate it from the tip of the tail
    head = np.ones_like(image)
    tx, ty = np.unravel_index(tail_distance.argmax(), tail_distance.shape)
    head[tx][ty] = 0
    h = np.ma.MaskedArray(head, mask)
    head_distance = skfmm.distance(h)
    # get the exact point
    hx, hy = np.unravel_index(head_distance.argmax(), head_distance.shape)
    body_points = (by, bx)
    tail_points = (ty, tx)
    head_points = (hy, hx)
    points = [body_points, tail_points, head_points]
    return distance, tail_distance, head_distance, points

"""function to send command to remote pi"""
def remote_pi_command(ip, port, username, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=port, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.readlines())

    finally:
        if ssh:
            ssh.close()

""" starts a remote cam server can be opened with vlc http://192.168.1.117:8000/stream.wmw"""
def remote_stream(ip, port, username, password):
    cmd = 'cvlc v4l2:///dev/video0 :v4l2-standard= :input-slave=alsa://hw:0,0 :live-caching=300 :sout="#transcode{vcodec=WMV2,vb=800,scale=1,acodec=wma2,ab=128,channels=2,samplerate=44100}:http{dst=:8000/stream.wmv}"'
    remote_pi_command(ip, port=port, username=username, password=password, command=cmd)

""" ends the stream by killing vlc """
def end_remote_stream(ip, port, username, password):
    cmd = 'pkill vlc'
    remote_pi_command(ip, port=port, username=username, password=password, command=cmd)






### TEST AREA ###
# fg = cv2.imread('/home/nicoluarte/Downloads/foreground.jpeg')
# bg = cv2.imread('/home/nicoluarte/Downloads/background.jpeg')
# final_image = image_full_process(bg, fg)
# body, tail, head, points = body_tracking(final_image)
remote_stream('192.168.1.117', '22', 'pi', 'dw4yb26f')
end_remote_stream('192.168.1.117', '22', 'pi', 'dw4yb26f')

### DISPLAY AREA ###
# plt.imshow(head)
# plt.scatter(*zip(*points))
# plt.show()

