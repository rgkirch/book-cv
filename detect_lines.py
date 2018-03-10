import cv2 as cv
import sys
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
import json
import math


def average_chain_lengths(l):
    if len(l) > 0:
        a = l[0]
        c = 1
        for b in l[1:]:
            if b == a:
                c += 1
            else:
                break
        return c


def get(res, w, h):
    slope_data = []
    for slope in [math.tan(x / res * math.pi) for x in range(res)]:
        lines_data = []
        for offset in range(h):
            line_data = []
            for x, y in [(x, int(slope * x + .5)) for x in range(w)]:
                line_data.append(img[(y+offset) % h][x])
            lines_data.append(average_chain_lengths(line_data))
        slope_data.append(sum(lines_data) / len(lines_data))
    return slope_data


data = None
res = 20

arg = sys.argv[1]
if arg.endswith('data'):
    with open(arg, 'r') as file:
        data = json.loads(file.readline())
    res = len(data)
else:
    img = cv.imread(arg, 0)
    img = cv.adaptiveThreshold(
        img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    # print(img[0][0:2])
    h, w = img.shape[:2]

    data = get(res, w, h)
    with open('detect-lines-{}.data'.format(res), 'w') as file:
        file.write(json.dumps(data))

# print("data")
# print(data)
# print("segs")
# print(segment_lengths)
# cv.imshow('img', img)
# cv.imshow('transs', np.transpose(img))

plt.plot([x/res*360 for x in range(res)], data)
plt.show()

# cv.waitKey(0)
