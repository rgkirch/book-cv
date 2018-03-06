import matplotlib.pyplot as plt
# from imutils import paths
import json
import cv2


levels = []
cap = cv2.VideoCapture('vid.mp4')
n = 0
try:
    while(1):
        n += 1
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.Laplacian(gray, cv2.CV_64F).var()
        levels.append(blur)
except:
    print(n)
    pass

plt.plot(levels)
plt.ylabel('some numbers')
plt.show()
with open("vid-data.txt", "w") as file:
    file.write(json.dumps(levels))
