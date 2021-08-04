import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('lena.jpg',1)
img2=cv.cvtColor(img,cv.COLOR_BGR2RGB)

cv.imshow('image',img)
plt.imshow(img2)
plt.xticks([]),plt.yticks([])
plt.show()
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()