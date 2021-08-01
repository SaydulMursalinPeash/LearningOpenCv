import cv2 as cv
import numpy as np


img=cv.imread('gradient.png',-1)
a,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
b,th2=cv.threshold(img,127,255,cv.THRESH_TOZERO)
cv.imshow('original',img)
cv.imshow('image',th1)
cv.imshow('th2',th2)

cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
