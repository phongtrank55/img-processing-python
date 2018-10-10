import cv2
#import numpy as np

img = cv2.imread("Image/hoasung.jpg", 1)

px = img[100, 80]

print(px)
print ("Size and channel: "+ str(img.shape))


b = img.item(100, 80, 0)
g = img.item(100, 80, 1)
r = img.item(100, 80, 2)
print("R = %d, G = %d, B=%d" %(r, g, b))


# cv2.waitKey()
# cv2.destroyAllWindows()