#!/usr/local/bin/python3.7
import cv2, time, cvlib
import matplotlib.pyplot as plt
from cvlib.object_detection import draw_bbox

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    frame = cv2.flip(frame, 1)
    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Camera", gray)

    key = cv2.waitKey(1)
    if(key == ord('\x1b')): #ESC
        break

video.release()
cv2.destroyAllWindows()
