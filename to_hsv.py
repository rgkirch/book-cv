import cv2
import numpy as np
import imageio

cap = cv2.VideoCapture('vid.mp4')
writer = imageio.get_writer('hsv.mp4', fps=30)
while(cap.isOpened()):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv[:, :, 1] = 255
    hsv[:, :, 2] = 255
    frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    writer.append_data(frame)

cap.release()
writer.close()
cv2.destroyAllWindows()
