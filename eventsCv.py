import cv2
import numpy as np

# img=np.zeros((512,512,3),np.uint8)
img = cv2.imread('messi5.jpg', -1)


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, '', y)
        txt = str(x) + '  ' + str(y)
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(img, txt, (x, y), font, 0.5, (255, 255, 0), 1)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        txt = str(blue) + ', ' + str(green) + ', ' + str(red)
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(img, txt, (x, y), font, 0.5, (255, 255, 255), 1)
        cv2.imshow('image', img)


cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
