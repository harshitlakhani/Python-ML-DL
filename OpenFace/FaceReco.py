#import library
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')

def detect_face(frame):
    cordinates = []
    t_list = []
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4) #face detection
    for x,y,w,h in faces:
        x1=x;x2=y;x3=x1+w;x4=x2+h
        t_list=[x1,x2,x3,x4]
        cordinates.append(t_list)
        color = (0,255,0)
        stroke = 1
        cv2.rectangle(frame,(x1,x2),(x3,x4),color,stroke) #draw rectangle arround faces
    return cordinates #cordinates of detected images

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    faces =  detect_face(frame) 
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()