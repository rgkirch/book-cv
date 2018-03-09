import cv2 as cv
import sys
import matplotlib.pyplot as plt
from collections import defaultdict


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
    segment_lengths = sorted(set([int(w / (x+1))
                                  for x in range(h)]), reverse=True)
    data = []
    for segment_length in segment_lengths:
        num_changes = 0
        # print("segment", segment_length)
        # print("hi")
        for y_offset in range(h):
            # print("y_offset", y_offset)
            s = sorted(
                set([x // segment_length for x in range(w)]), reverse=True)
            # print(s)
            pxs = []
            for e in s:
                pxs.extend(img[(e+y_offset) % h]
                           [e*segment_length: (e+1)*segment_length])
            num_changes += f(pxs)
        data.append(num_changes)
    return (data, segment_lengths)


img = cv.imread(sys.argv[1], 0)
img = cv.adaptiveThreshold(
    img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
# print(img[0][0:2])
h, w = img.shape[:2]
data, segment_lengths = get(w, h)
print("data")
print(data)
print("segs")
print(segment_lengths)
cv.imshow('img', img)
plt.plot(segment_lengths, [k / h for k in data])
plt.show()
# cv.waitKey(0)
