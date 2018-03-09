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
    segment_lengths = sorted(set([w // x
                                  for x in range(1, h)]), reverse=True)
    segment_lengths += sorted(set([w //
                                   x for x in range(-h, 0)]), reverse=True)
    data = []
    for segment_length in segment_lengths:
        num_changes = 0
        # print("segment", segment_length)
        # print("hi")
        for y_offset in range(h):
            # print("y_offset", y_offset)
            for row_y_start in range(w//segment_length):
                pxs = []
                pxs.extend(img[(row_y_start+y_offset) % h][row_y_start *
                                                           segment_length: (row_y_start+1)*segment_length])
                num_changes += f(pxs)
        data.append(num_changes)
    return (segment_lengths, data)


img = cv.imread(sys.argv[1], 0)
img = cv.adaptiveThreshold(
    img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
# print(img[0][0:2])
h, w = img.shape[:2]
segment_lengths, data = get(w, h)
print("data")
print(data)
print("segs")
print(segment_lengths)
cv.imshow('img', img)
plt.plot(segment_lengths, [k / h for k in data])
plt.show()
# cv.waitKey(0)
