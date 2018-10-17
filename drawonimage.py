import cv2
import numpy as np

img = cv2.imread('Image/hoasung.jpg', 1)

cv2.line(img, (0, 0), (150, 150), (255, 0, 0), 15)


cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)

cv2.circle(img, (100, 63), 55, (0, 0, 255), 0) #<0 la tô

points = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32);
# points = points.reshape((-1, 1, 2))
# print(points);
cv2.polylines(img, [points], True, (0, 255, 255), 3) # True: Thanh vong tron

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Learn opencv',(50, 130), font, 1, (255, 255, 0), 2, cv2.LINE_AA) # 1 là cỡ chữ; 2 là độ đậm nét



cv2.imshow('Hoa sung', img)

cv2.waitKey()
cv2.destroyAllWindows()
