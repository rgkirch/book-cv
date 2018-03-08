#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import sys
import json


def f(l):
    if len(l) > 0:
        a = l[0]
        c = 1
        for b in l[1:]:
            if b == a:
                c += 1
        return c


img = cv.imread(sys.argv[1], 0)
img = cv.adaptiveThreshold(
    img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
# cv.imshow('image', img)
print(img.shape)
h, w = img.shape[:2]
npdata = np.zeros((h, w), np.uint16)
data = [[] for _ in range(h)]
for y, row in enumerate(img):
    while(len(row) > 0):
        x = f(row)
        data[y] += [x]*x
        row = row[x:]

with open('analyze.data', 'w') as file:
    file.write(json.dumps(data))


# cv.imshow('img', img)
plt.imshow(data)
plt.colorbar()
plt.show()
# cv.waitKey(0)
# cv.destroyAllWindows()
