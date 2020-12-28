#!/usr/local/bin/python3.7
import numpy as np
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(im, bbox, label, conf)

    cv2.imshow('output',output_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
