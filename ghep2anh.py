import cv2

img1 = cv2.imread('Image/hoasung.jpg', 1)
img2 = cv2.imread('Image/hoamai.jpg', 1)

# 2 anh co cung kich thuoc, cung kenh
img1 = img1[100:300, 100:350]
img2 = img2[100:300, 100:350]

imgRes = cv2.add(img1, img2)

cv2.imshow('Anh 1', img1)
cv2.imshow('Anh 2', img2)
cv2.imshow('Ket qua', imgRes)


cv2.waitKey()
cv2.destroyAllWindows()