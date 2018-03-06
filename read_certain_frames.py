import cv2
import json

frames = []
with open('frames-i-care-about.txt', 'r') as file:
    frames = json.loads(file.readline())

cap = cv2.VideoCapture('vid.mp4')
n = 0
try:
    while(1):
        ret, frame = cap.read()
        if(n == frames[0]):
            # cv2.imshow('frame', frame)
            number = '0'*(4-len(str(n)))
            name = 'caps/frame-' + number + str(n) + '.png'
            cv2.imwrite(name, frame)
            # cv2.waitKey(0)
            frames.pop(0)
        n += 1
except:
    print(n)
    pass
