import cv2
import numpy as  np


img1 = cv2.imread('Image/hoasung.jpg', 1)
img2 = cv2.imread('Image/hoamai.jpg', 1)
size_img1 = img1.shape
img2 = cv2.resize(img2, (size_img1[1], size_img1[0]))

# add = img1 + img2

add = cv2.add(img1, img2) # Gia tri > 255 se chuyen ve 255

weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) # Tron

# cv2.imshow('ADD', add)

cv2.imshow('weighted', weighted)
cv2.waitKey()
cv2.destroyAllWindows()
