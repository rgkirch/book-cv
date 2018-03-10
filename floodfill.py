#!/usr/bin/env python
import numpy as np
import cv2 as cv
import sys


def update(dummy=None):
    iters = cv.getTrackbarPos('iters', 'image')
    sz = cv.getTrackbarPos('sz', 'image')
    if seed_pt is None:
        cv.imshow('image', img)
        return
    copy = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    mask[:] = 0
    cv.floodFill(copy, mask, seed_pt, (200, 50, 50),
                 (1,)*3, (1,)*3, cv.FLOODFILL_FIXED_RANGE | 4 | (255 << 8))
    cv.imshow('image', copy)


def onmouse(event, x, y, flags, param):
    global seed_pt
    if flags & cv.EVENT_FLAG_LBUTTON:
        seed_pt = x, y
        update()


img = cv.imread(sys.argv[1], 0)
img = cv.adaptiveThreshold(
    img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
h, w = img.shape
mask = np.zeros((h+2, w+2), np.uint8)
seed_pt = None
update()
cv.createTrackbar('sz', 'image', 2, 10, update)
cv.createTrackbar('iters', 'image', 1, 10, update)
cv.setMouseCallback('image', onmouse)

cv.waitKey(0)
cv.destroyAllWindows()
