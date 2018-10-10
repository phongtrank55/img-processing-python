import cv2;
# import numpy as np

src = cv2.imread('Image/hoasung.jpg', 1)

# Thong tin anh: chieu cao, chieu rong va so luong kenh mau
print('Thong tin anh: ', src.shape)

print('Chieu cao: ', src.shape[0])

# Kich thuoc anh (dung luong)
print('Size: ', src.size, 'byte ')

#boi den diem chon
cv2.rectangle(src, (100, 50), (400, 250), (0,255,0), 1)
cv2.imshow('Anh goc', src)
#Cat anh
subImg = src[50:250, 100:400] #  y, x
cv2.imshow('Sub image', subImg)

#Doi kenh mau
subImg = subImg[:, :, 2] # Doi toan bo sang kenh R
cv2.imshow('Sub image', subImg)


cv2.waitKey()
cv2.destroyAllWindows()

