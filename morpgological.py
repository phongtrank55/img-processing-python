import cv2
import numpy as  np

cap = cv2.VideoCapture(0)

kernel = np.ones((5, 5), np.uint8)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([6, 7, 8])
	upper_red = np.array([255, 255, 255])

	# dark_red = np.unit8([[[12, 22, 121]]])
	# dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)	

	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	erosion = cv2.erode(mask, kernel, iterations = 1) # co
	dilation = cv2.dilate(mask, kernel, iterations = 1) #Gian

	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

	cv2.imshow('Frame', frame)
	# cv2.imshow('mask', mask)
	# cv2.imshow('Res', res)
	cv2.imshow('erosion', erosion)
	cv2.imshow('dilation', dilation)
	cv2.imshow('opening', opening)
	cv2.imshow('closing', closing)

	k = cv2.waitKey(5) & 0xFF 
	if k == 27: # ESC
		break
	
# print(kernel)
cv2.destroyAllWindows()
cap.release()
