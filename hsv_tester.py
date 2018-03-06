import cv2
import numpy as np
import imageio

frame = cv2.imread('img.png')
hue = 0
saturation = 0
value = 0


def hue_callback(x):
    global hue
    hue = x
    update()


def saturation_callback(x):
    global saturation
    saturation = x
    update()


def value_callback(x):
    global value
    value = x
    update()


def update():
    global frame
    global hue
    global saturation
    global value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv[:, :, 0] = hue
    hsv[:, :, 1] = saturation
    hsv[:, :, 2] = value
    frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('win', frame)


cv2.namedWindow('win')
cv2.createTrackbar('hue', 'win', 0, 180, hue_callback)
cv2.createTrackbar('saturation', 'win', 0, 255, saturation_callback)
cv2.createTrackbar('value', 'win', 0, 255, value_callback)
cv2.waitKey(0)

cv2.destroyAllWindows()
