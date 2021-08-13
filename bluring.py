#%%
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread("opencv-logo.png",-1)
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()


# %%
