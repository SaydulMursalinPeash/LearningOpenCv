import cv2
import numpy as np

# img=cv2.imread('lena.jpg',-1)


img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5)
img = cv2.arrowedLine(img, (255, 0), (255, 300), (0, 0, 255), 10)
img = cv2.rectangle(img, (0, 0), (255, 255), (0, 255, 0), 3)
img = cv2.circle(img, (300, 300), 50, (12, 100, 150), 5)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv learning', (255, 300), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
if k == ord('x'):
    cv2.destroyAllWindows()
