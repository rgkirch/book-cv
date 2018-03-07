import cv2
import numpy as np
import imageio

frame = cv2.imread('img.png')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
img = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('win', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
