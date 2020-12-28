#!/usr/local/bin/python3.7
import cv2
import matplotlib.pyplot as plt
import cvlib
from cvlib.object_detection import draw_bbox

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("Capturing", frame)
    cv2.imwrite(filename='webcap.jpg', img=frame)
    im  =  cv2.imread('webcap.jpg')
    bbox, label, conf  =  cvlib.detect_common_objects(im)
    output_image = draw_bbox(im , bbox , label , conf)
    plt.imshow(output_image)
    plt.show()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
