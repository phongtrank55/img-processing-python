import cv2
import numpy as  np

cap = cv2.VideoCapture(0)

kernel = np.ones((5, 5), np.uint8)

while True:
	_, frame = cap.read()
	
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

	edges = cv2.Canny(frame, 59, 200)

	cv2.imshow('Frame', frame)
	cv2.imshow('Laplacian', laplacian)
	cv2.imshow('Sobel X', sobelx)
	cv2.imshow('Sobel Y', sobely)

	cv2.imshow('Edges', edges)
	

	k = cv2.waitKey(5) & 0xFF 
	if k == 27: # ESC
		break
	
# print(kernel)
cv2.destroyAllWindows()
cap.release()
