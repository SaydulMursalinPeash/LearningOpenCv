import cv2
import numpy as np

img = cv2.imread('messi5.jpg', -1)

ball=img[280:340,330:390]
img[273:333,100:160]=ball
cv2.imshow('orange', img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
