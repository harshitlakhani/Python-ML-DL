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
       

print("Select the option.")
print("1. Canny Edge Detection")
print("2. Sobel Derivatives")

opp = int(input("OPTION:"))
if opp == 1:
    CannyEdgeDetector()
elif opp == 2:
    pass
else:
    print("Wrong option selected! Try Again")


 
