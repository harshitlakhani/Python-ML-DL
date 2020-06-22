import numpy as np
import cv2
import pickle
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

os.chdir('D:\GitHub\Algorithms---Python\openCV\Face Recognition\images\harshit')


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)
inter, count= 0,0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)
    for (x, y, w, h) in faces:
        gray_img = gray[y:y+h+15, x:x+w+15]
        if(inter%5 == 0):
            cv2.imwrite(str(count) + '.jpg',gray_img)
            count+=1
        inter+=1
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
