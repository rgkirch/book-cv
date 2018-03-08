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
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (sz, sz))
    copy = img.copy()
    mask[:] = 0
    # cv.bitwise_and(flooded, flooded, mask=mask)
    # green.copy_to(flooded, mask)
    copy = cv.morphologyEx(copy, cv.MORPH_CLOSE, kernel)
    copy = cv.erode(copy, kernel, iterations=iters)
    cv.floodFill(copy, mask, seed_pt, (255, 255, 255),
                 (1,)*3, (1,)*3, cv.FLOODFILL_FIXED_RANGE | 4 | (255 << 8))
    cv.circle(copy, seed_pt, 2, (0, 0, 255), -1)
    cv.circle(mask, seed_pt, 2, (0, 0, 255), -1)
    # cv.imshow('floodfill', flooded)
    cv.imshow('mask', mask)
    cv.imshow('copy', copy)


def onmouse(event, x, y, flags, param):
    global seed_pt
    if flags & cv.EVENT_FLAG_LBUTTON:
        seed_pt = x, y
        update()


img = cv.imread(sys.argv[1], 0)
img = cv.adaptiveThreshold(
    img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
h, w = img.shape[:2]
green = np.zeros((w, h, 3), np.uint8)
green[:] = (0, 255, 0)
mask = np.zeros((h+2, w+2), np.uint8)
seed_pt = None
update()
cv.createTrackbar('sz', 'image', 3, 10, update)
cv.createTrackbar('iters', 'image', 1, 10, update)
cv.setMouseCallback('image', onmouse)
cv.setMouseCallback('mask', onmouse)
cv.setMouseCallback('copy', onmouse)

cv.waitKey(0)
cv.destroyAllWindows()
