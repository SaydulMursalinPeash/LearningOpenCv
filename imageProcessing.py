import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread('lena.jpg',-1)
img1=cv2.resize(img1,(512,512))
img2=cv2.imread('orange.jpg',-1)
img2=cv2.resize(img2,(512,512))
img3=cv2.add(img1,img2)
cv2.imshow("AddedImage",img3)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
img4=cv2.addWeighted(img1,0.3,img2,0.7,0)
cv2.imshow('addweighted',img4)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

