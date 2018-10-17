import cv2
import numpy as  np


img1 = cv2.imread('Image/hoasung.jpg', 1)
img2 = cv2.imread('Image/hoamai.jpg', 1)

rows, cols, channels = img1.shape

roi = img2[:rows, :cols]

img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# print(img1gray[0][1])
result, mask = cv2.threshold(img1gray, 200, 255, cv2.THRESH_BINARY_INV)
# print(img1gray[0][1])
# print(mask)
mask_inv = cv2.bitwise_not(mask)

# img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

img1_fg = cv2.bitwise_and(img1, img1, mask=mask)
cv2.imshow('img1_bg', img1_fg)
cv2.waitKey()
cv2.destroyAllWindows()
