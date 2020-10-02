#!/home/nicoluarte/uni/PHD/tracking_device/environments/bg_fg/bin/python3.8
from bg_fg import *

take_background('/home/nicoluarte/uni/PHD/tracking_device/background.png')

""" function only made to show an animation """
def update(i):
    p.set_data(live_preview(cap, bg))
    n.set_offsets(live_points(cap, bg))
cap = cv2.VideoCapture(0)
bg = cv2.imread('/home/nicoluarte/Downloads/bg2.png')
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

