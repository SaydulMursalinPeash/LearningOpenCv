import cv2 as cv

img=cv.imread('sudoku.png',0)

cv.imshow('original',img)
a,th=cv.threshold(img,50,255,cv.THRESH_BINARY)
th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
cv.imshow('res',th)
cv.imshow('res2',th2)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()

