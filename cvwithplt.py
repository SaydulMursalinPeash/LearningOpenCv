import cv2 as cv
import matplotlib.pyplot as plt


img=cv.imread('lena.jpg',-1)
cv.imshow('image',img)





cv.waitKey(0) & 0xFF
cv.destroyAllWindows()