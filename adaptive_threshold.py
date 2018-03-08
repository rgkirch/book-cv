import cv2 as cv
import numpy as np
import imageio


cap = cv.VideoCapture('vid.mp4')
writer = imageio.get_writer('adaptive-threshold.mp4', fps=30)
while(cap.isOpened()):
    _, frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.adaptiveThreshold(
        frame, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    frame = cv.cvtColor(frame, cv.COLOR_GRAY2BGR)
    writer.append_data(frame)

cap.release()
writer.close()
