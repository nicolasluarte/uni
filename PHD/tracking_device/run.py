#!/home/nicoluarte/uni/PHD/tracking_device/environments/bg_fg/bin/python3.8
from bg_fg import *
import os
import glob


take_background('/home/nicoluarte/Downloads/rat_video/Non_annotated/redlight/rat_01_seq_01_redlight/Frames_2017_10_20_09_13_25/000000000_000000000_d.png')

""" function only made to show an animation """
def update(i):
    p.set_data(live_preview(cap, bg))
    n.set_offsets(live_points(cap, bg))
cap = cv2.VideoCapture(0)

# load all images from a folder
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return image


bg = cv2.imread('/home/nicoluarte/Downloads/background.jpeg')
points = live_points(cap, bg)
p = plt.imshow(live_preview(cap, bg))
n = plt.scatter(*zip(*points), marker="x", color="red")
ani = FuncAnimation(plt.gcf(), update, interval=50)
plt.show()
cap.release()
cv2.destroyAllWindows()

take_background('/home/nicoluarte/Downloads/bg2.png')
bg = cv2.imread('/home/nicoluarte/Downloads/background.png')
fg = cv2.imread('/home/nicoluarte/Downloads/fg2.png')
fg2 = cv2.imread('/home/nicoluarte/uni/PHD/tracking_device/foreground2.png')
frame, tail, head, points = body_tracking(image_full_process(bg, fg))
plt.imshow(frame)
plt.scatter(*zip(*points), marker="x", color="red")
plt.show()

plt.imshow(contour_extraction(postprocess_image(bgfg_diff(bg, fg))), cmap='gray')
plt.show()


img_list = glob.glob('/home/nicoluarte/Downloads/rat_video/Non_annotated/redlight/rat_01_seq_01_redlight/Frames_2017_10_20_09_13_25/*_*_c.png')

for i in range(len(img_list)):
    bg = cv2.imread('/home/nicoluarte/Downloads/background.jpeg')
    fg = cv2.imread(img_list[i])
    frame, tail, head, points = body_tracking(image_full_process(bg, fg))
    plt.imshow(fg)
    plt.scatter(*zip(*points), marker="x", color="red")
    plt.draw()
    plt.pause(0.0001)
    plt.clf()

def animation(i):
    img_list = glob.glob('/home/nicoluarte/Downloads/rat_video/Non_annotated/redlight/rat_01_seq_01_redlight/Frames_2017_10_20_09_13_25/*_*_c.png')
    data = []
    markers = []
    for image in img_list:





test(cap, bg, 100)

### TEST AREA ###
# final_image = image_full_process(bg, fg)
# body, tail, head, points = body_tracking(final_image)
# remote_stream('192.168.1.117', '22', 'pi', 'dw4yb26f')
# end_remote_stream('192.168.1.117', '22', 'pi', 'dw4yb26f')

### DISPLAY AREA ###
# plt.imshow(head)
# plt.scatter(*zip(*points))
# plt.show()

