import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img=cv.imread('opencv-logo.png',1)
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
kernal=np.ones((5,5),np.float32)/25
dst=cv.filter2D(img,-1,kernal)


titles=['image','2D convulation']
images=[img,dst]


for i in range(2):
    plt.subplot(2,2,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
