import cv2

img = cv2.imread('Image/hoasung.jpg', 1)
cv2.imshow('Hoa sung', img)
cv2.waitKey()
cv2.destroyAllWindows()
