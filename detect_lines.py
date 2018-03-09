import cv2 as cv
import sys
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
import math


def f(l):
    if len(l) > 0:
        a = l[0]
        c = 1
        for b in l[1:]:
            if b == a:
                c += 1
            else:
                break
        return c


def get(w, h):
    res = 100
    the = []
    for slope in [math.tan(x / res * math.pi) for x in range(res)]:
        data = []
        for offset in range(h):
            for x, y in [(x, int(slope * x + .5)) for x in range(w)]:
                data.append(img[(y+offset) % h][x])
        the.append(data)
    return the


img = cv.imread(sys.argv[1], 0)
img = cv.adaptiveThreshold(
    img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
# print(img[0][0:2])
h, w = img.shape[:2]
data = get(w, h)
# print("data")
# print(data)
# print("segs")
# print(segment_lengths)
# cv.imshow('img', img)
# cv.imshow('transs', np.transpose(img))
plt.plot(data)
plt.show()
# cv.waitKey(0)
