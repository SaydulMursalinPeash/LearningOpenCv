import cv2 as cv

import numpy as np
def posi(x):
    print(x)
img=np.zeros((250,250,3),np.uint8)
cv.namedWindow('Trackb')
cv.createTrackbar('B','Trackb',0,255,posi)
cv.createTrackbar('G','Trackb',0,255,posi)
cv.createTrackbar('R','Trackb',0,255,posi)

while True:
    cv.imshow('Trackb',img)
    k=cv.waitKey(1) & 0xFF
    if k==27:
        break
    
    b=cv.getTrackbarPos('B','Trackb')
    g=cv.getTrackbarPos('G','Trackb')
    r=cv.getTrackbarPos('R','Trackb')

    img[:]=[b,g,r]




cv.waitKey(0) & 0xFF
cv.destroyAllWindows()