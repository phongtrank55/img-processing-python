import cv2
import numpy as np

img = cv2.imread('Image/hoasung.jpg', 1)

temp = img[100:200, 120:190]

img[:100, :70] = temp # paste

cv2.imshow('Hoa sung', img)
cv2.waitKey()
cv2.destroyAllWindows()
