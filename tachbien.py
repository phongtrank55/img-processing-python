import cv2

img = cv2.imread('Image/person.jpg', 0)

img2 = cv2.Canny(img, 200,250)

cv2.imshow('Anh goc', img2)
cv2.waitKey()
cv2.destroyAllWindows()
