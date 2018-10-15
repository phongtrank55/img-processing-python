import cv2

print(cv2.__version__)

vidcap = cv2.VideoCapture('../Video/video1.mp4')

# success, image = vidcap.read()

count = 0


while True:
	success, image = vidcap.read()
	if not success:
		break
	cv2.imwrite('../Video/imgvideo1/frame%d.jpg' % count, image)
	
	print ('Success frame ', count)
	count += 1


