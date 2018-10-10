import cv2;
import numpy as np;

rgb = np.uint8([[[77, 177, 35]]])

hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)

print(hsv) # [[[ 69 205 177]]]

imgSrc = cv2.imread('Image/multicolor.jpg', 1);
cv2.imshow('Anh goc', imgSrc)

hsvImg = cv2.cvtColor(imgSrc, cv2.COLOR_BGR2HSV)
cv2.imshow('Anh HSV', hsvImg)

# Dat nguong
min_color =  np.array([ 67, 205, 177])
max_color = np.array([71, 205, 177])

# mat na loc
mask = cv2.inRange(hsvImg, min_color, max_color)
# print(mask)
cv2.imshow('Mat na', mask)

imgRes = cv2.bitwise_and(imgSrc, imgSrc, mask = mask)
cv2.imshow('Ket qua', imgRes)

# print(mask.shape)
# print(imgSrc.shape)

cv2.waitKey()
cv2.destroyAllWindows()