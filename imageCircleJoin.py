import cv2
import numpy as np

img = np.zeros((255, 255, 3), np.uint8)


def click_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 255, 0), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 2)
        cv2.imshow('image', img)


points = []
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_callback)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
