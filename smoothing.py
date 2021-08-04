import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img=cv.imread('opencv-logo.png',1)
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

titles=['image']
images=[img,]
