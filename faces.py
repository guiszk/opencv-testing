#!/usr/local/bin/python3.7
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml') #FACE
smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_profileface.xml') #SMILE
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml') #EYES
cat_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalcatface_extended.xml') #CAT


cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for(x, y, w, h) in faces:
        print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        img_item = "face.png"
        cv2.imwrite(img_item, roi_gray)

        color = (0, 0, 255) #BGR
        stroke = 2 #thickness
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        font = cv2.FONT_HERSHEY_SIMPLEX
        name = "face"
        color = (255, 255, 255)
        stroke = 2
        cv2.putText(frame, name, (x, y), font, 0.9, color, stroke, cv2.LINE_AA)

    smile = smile_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for(x, y, w, h) in smile:
        print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        img_item = "cat.png"
        cv2.imwrite(img_item, roi_gray)

        color = (255, 255, 0) #BGR
        stroke = 2 #thickness
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        font = cv2.FONT_HERSHEY_SIMPLEX
        name = "smile"
        color = (255, 255, 255)
        stroke = 2
        cv2.putText(frame, name, (x, y), font, 0.9, color, stroke, cv2.LINE_AA)


    eye = eye_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for(x, y, w, h) in eye:
        print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        img_item = "eye.png"
        cv2.imwrite(img_item, roi_gray)

        color = (0, 255, 0) #BGR
        stroke = 2 #thickness
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        font = cv2.FONT_HERSHEY_SIMPLEX
        name = "eye"
        color = (255, 255, 255)
        stroke = 2
        cv2.putText(frame, name, (x, y), font, 0.9, color, stroke, cv2.LINE_AA)

    cat = cat_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for(x, y, w, h) in cat:
        print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        img_item = "cat.png"
        cv2.imwrite(img_item, roi_gray)

        color = (255, 0, 0) #BGR
        stroke = 2 #thickness
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        font = cv2.FONT_HERSHEY_SIMPLEX
        name = "cat"
        color = (255, 255, 255)
        stroke = 2
        cv2.putText(frame, name, (x, y), font, 0.9, color, stroke, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    if(cv2.waitKey(20) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
