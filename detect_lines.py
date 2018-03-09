import cv2 as cv
import sys
import matplotlib.pyplot as plt


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
    all_data = []
    for segment_length in sorted(set([int(w / (x+1)) for x in range(h)]), reverse=True):
        # print("segment", segment_length)
        one_slope_data = []
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
            one_slope_data.append(f(pxs))
        all_data.append(sum(one_slope_data) / len(one_slope_data))
    return all_data


img = cv.imread(sys.argv[1], 0)
img = cv.adaptiveThreshold(
    img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
# print(img[0][0:2])
h, w = img.shape[:2]
data = get(w, h)
plt.plot(data)
plt.show()
