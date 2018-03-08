#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import sys
import json


def update(dummy=None):
    wide = cv.getTrackbarPos('wide', 'img')
    tall = cv.getTrackbarPos('tall', 'img')
    wide_kernel = np.ones((1, wide))
    tall_kernel = np.ones((tall, 1))
    wide_img = cv.bitwise_not(cv.dilate(cv.bitwise_not(img), wide_kernel))
    tall_img = cv.bitwise_not(cv.dilate(cv.bitwise_not(img), tall_kernel))
    or_img = cv.bitwise_not(cv.bitwise_or(
        cv.bitwise_not(wide_img), cv.bitwise_not(tall_img)))
    cv.imshow('img', img)
    cv.imshow('wide_img', wide_img)
    cv.imshow('tall_img', tall_img)
    cv.imshow('or_img', or_img)


img = cv.imread(sys.argv[1], 0)
img = cv.adaptiveThreshold(
    img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow('img', img)
cv.createTrackbar('wide', 'img', 1, 10, update)
cv.createTrackbar('tall', 'img', 1, 10, update)
update()
cv.waitKey(0)
