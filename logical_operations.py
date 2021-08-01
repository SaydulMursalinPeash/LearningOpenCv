import cv2
import numpy as np

img1= np.zeros((510,510),np.uint8)
img2=np.zeros((510,510),np.uint8)

img1=cv2.rectangle(img1,(0,0),(255,510),(255,255,255),-1)
img2=cv2.rectangle(img2,(220,0),(510,510),(255,255,255),-1)

img3=cv2.bitwise_xor(img1,img2)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

