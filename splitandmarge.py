import cv2
import numpy as np

img=cv2.imread('fruits.jpg',-1)
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

cv2.imshow('image',img)
cv2.waitKey(0) & 0xFF
cv2.destroyWindow()