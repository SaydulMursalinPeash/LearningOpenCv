import cv2 as cv
import numpy as np

def nothing(x):
    pass

cap=cv.VideoCapture(0)
background=0

for i in range(30):
    ret,background=cap.read()

background=np.flip(background,axis=1)

LB=cv.createTrackbar('LB','Tracker',0,255,nothing)
LG=cv.createTrackbar('LG','Tracker',0,255,nothing)
LR=cv.createTrackbar('LR','Tracker',0,255,nothing)
UB=cv.createTrackbar('UB','Tracker',0,255,nothing)
UG=cv.createTrackbar('UG','Tracker',0,255,nothing)
UR=cv.createTrackbar('UR','Tracker',0,255,nothing)


while True:
    a,frame=cap.read()
    frame =np.flip(frame,axis=1)
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    lb=cv.getTrackbarPos('LB','Tracker')
    lg=cv.getTrackbarPos('LG','Tracker')
    lr=cv.getTrackbarPos('LR','Tracker')
    ub=cv.getTrackbarPos('UB','Tracker')
    ug=cv.getTrackbarPos('UG','Tracker')
    ur=cv.getTrackbarPos('UR','Tracker')

    l_b= np.array([lb,lg,lr])
    u_b=np.array([ub,ug,ur])
    mask=cv.inRange(hsv,l_b,u_b)

    

    cv.imshow('video',frame)
    cv.imshow('background',background)
    k=cv.waitKey(1) & 0xFF

    if k==ord('x'):
        break
cap.release()
cv.destroyAllWindows()

