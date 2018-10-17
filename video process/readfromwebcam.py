import cv2
# import numpy as np

cap = cv2.VideoCapture(0) #Lay webcam
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('../Video/VideoWebcam.avi', fourcc, 10.0, (640, 480 )) #Stream ghi video


while True:
	success, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	if not success:
		print('Khong doc dc')
		break

	out.write(frame)
	cv2.imshow('frame', frame)
	cv2.imshow('GRAY', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'): #An nut q de thoat
		break

cap.release()
cv2.destroyAllWindows()
