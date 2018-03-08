#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import sys
import json


img = cv.imread(sys.argv[1], 0)
wide = np.ones((1, 5))
print(wide)
tall = np.ones((5, 1))
print(tall)
img = cv.adaptiveThreshold(
    img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
# img = cv.morphologyEx(img, cv.MORPH_OPEN, np.ones((2, 2)))
cv.imshow('img', img)
wide = cv.bitwise_not(cv.dilate(cv.bitwise_not(img), wide))
tall = cv.bitwise_not(cv.dilate(cv.bitwise_not(img), tall))
cv.imshow('wide', wide)
cv.imshow('tall', tall)
bitwise_or = cv.bitwise_not(cv.bitwise_or(
    cv.bitwise_not(wide), cv.bitwise_not(tall)))
cv.imshow('or', bitwise_or)
cv.waitKey(0)
