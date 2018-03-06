import cv2
import numpy as np
import imageio

frame = cv2.imread('img.png')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
value = 128


def callback(x):
    global value
    value = x
    update()


def update():
    global gray
    global value
    _, img = cv2.threshold(gray, value, 255, cv2.THRESH_BINARY)
    cv2.imshow('win', img)


cv2.namedWindow('win')
cv2.createTrackbar('value', 'win', 0, 255, callback)
cv2.waitKey(0)

cv2.destroyAllWindows()
