import cv2
import numpy as np
import imageio

frame = cv2.imread('img.png')


def callback(h):
    global frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv[:, :, 0] = h
    frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('win', frame)


cv2.namedWindow('win')
cv2.createTrackbar('hue', 'win', 0, 180, callback)
cv2.waitKey(0)

cv2.destroyAllWindows()
