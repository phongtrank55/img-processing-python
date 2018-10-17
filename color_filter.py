import cv2
import numpy as  np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([5, 0, 0])
	upper_red = np.array([255, 255, 255])

	# dark_red = np.unit8([[[12, 22, 121]]])
	# dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)	

	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	cv2.imshow('Frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('Res', res)

	k = cv2.waitKey(5) & 0xFF 
	if k == 27: # ESC
		break
	

cv2.destroyAllWindows()
cap.release()
