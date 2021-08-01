import cv2 as cv
import numpy as np


def nothing(x):
    pass

cv.namedWindow('Tracker')
cap=cv.VideoCapture(0)
LB=cv.createTrackbar('LB','Tracker',0,255,nothing)
LG=cv.createTrackbar('LG','Tracker',0,255,nothing)
LR=cv.createTrackbar('LR','Tracker',0,255,nothing)
UB=cv.createTrackbar('UB','Tracker',0,255,nothing)
UG=cv.createTrackbar('UG','Tracker',0,255,nothing)
UR=cv.createTrackbar('UR','Tracker',0,255,nothing)


while True:
    a,frame=cap.read()
    #img=cv.imread('smarties.png',-1)
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lb=cv.getTrackbarPos('LB','Tracker')
    lg=cv.getTrackbarPos('LG','Tracker')
    lr=cv.getTrackbarPos('LR','Tracker')
    ub=cv.getTrackbarPos('UB','Tracker')
    ug=cv.getTrackbarPos('UG','Tracker')
    ur=cv.getTrackbarPos('UR','Tracker')

    l_b= np.array([lb,lg,lr])
    u_b=np.array([ub,ug,ur])
    print(l_b,u_b)

    mask= cv.inRange(hsv,l_b,u_b)
    res=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow('orriginal',frame)
    cv.imshow('mask',mask)
    cv.imshow('result',res)

    key=cv.waitKey(1) & 0xFF
    if key==27:
        break
cv.destroyAllWindows()

