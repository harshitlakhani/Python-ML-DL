#importing modules
import cv2
import numpy

def nothing(x):
    pass

def CannyEdgeDetector():
    #capturing the video from webcame
    capture = cv2.VideoCapture(0)

    cv2.namedWindow('Canny')


    cv2.createTrackbar('lower','Canny',50,255,nothing)
    cv2.createTrackbar('upper','Canny',50,255,nothing)

    #loop
    while(1):
        ret, frame = capture.read()

        lower = cv2.getTrackbarPos('lower','Canny')
        upper = cv2.getTrackbarPos('upper','Canny')

        edges = cv2.Canny(frame,lower,upper)

        cv2.imshow('Canny',edges)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    capture.release()
    cv2.destroyAllWindows()        

def SobelDerivatives():
    #capturing the video from the webcame
    capture = cv2.VideoCapture(0)

    while(1):
        ret, frame = capture.read()

        blur = cv2.GaussianBlur(frame,(5,5),0)

        img_gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        
        sobel = cv2.Sobel(img_gray,cv2.CV_64F,1,1,ksize=3)
        gray = cv2.convertScaleAbs(sobel, alpha=255/sobel.max())

        cv2.imshow('sobely',gray)

        k = cv2.waitKey(5) & 0xFF
        if k == 27: 
            break
    capture.release()
    cv2.destroyAllWindows()

print("Select the option.")
print("1. Canny Edge Detection")
print("2. Sobel Derivatives")

opp = int(input("OPTION:"))
if opp == 1:
    CannyEdgeDetector()
elif opp == 2:
    SobelDerivatives()
else:
    print("Wrong option selected! Try Again")


 
