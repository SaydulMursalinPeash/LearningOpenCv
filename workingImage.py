
import cv2

image=cv2.imread('lena.jpg',-1)
cv2.imshow('image',image)
k=cv2.waitKey(0) & 0xFF
print(ord('s'))
print(k)
if k==27:
    cv2.destroyAllWindows()

elif k==ord('s'):
    cv2.imwrite('lena2.png',image)
    cv2.destroyAllWindows()