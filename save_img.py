import cv2


src = cv2.imread("Image/hoasung.jpg", 1)
cv2.line(src, (0, 0), (400, 300), (255, 0, 0), 5)

cv2.imshow("Anh luu moi", src)
cv2.imwrite("Image/anhsaukhive.jpg", src)
cv2.waitKey()
cv2.destroyAllWindows()