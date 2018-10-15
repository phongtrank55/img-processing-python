import cv2
import numpy as np
# import matplotlib.pyplot as plt


img = cv2.imread('../Image/digits.PNG', 0)
testImg = cv2.imread('../Image/testchuviet2.PNG',0)
cv2.imshow('Anh kiem tra', testImg)

# print(img.shape)
# cv2.imshow('Anh goc - Xam', img)

# Anh 5000 ký tự, mỗi ký tự có cỡ 20x20
# Cat anh
cells =[np.hsplit(row, 100) for row in np.vsplit(img, 50)]
# des=cv2.imwrite('../Image/testchuviet2.PNG', cells[34][50])
# print(cells[48][96])
# cv2.imshow('Anh cat', cells[34][50])
# chuyen moi anh cat sang mang 1 chieu
x = np.array(cells) #ep kieu ve nparray
# print(x)
# x2 = x[0, 0].reshape(-1, 20*20)
# cv2.imshow('Anh cat', x2)

trainData = x[:, :50].reshape(-1, 20*20).astype(np.float32) # Nửa ảnh đầu 2500 ky tu so

imgTest = np.array(testImg).reshape(-1, 20*20).astype(np.float32) 
# print(imgTest)

# test = x[:, 50:100].reshape(-1, 20*20).astype(np.float32) # Nửa ảnh cuối de dư lieu test

# Cac nhan ket qua nhan dang
k = np.arange(10) # Ket qua la 0 den 9
# print(k)

trainLabels = np.repeat(k, 250)[:, np.newaxis] #Moi so k co 250 ky tu bieu dien. Chuyen sang chieu doc de gan vs trainData 

# print(trainLabels)
# print(np.newaxis) #None

# Huan luyen
knn = cv2.ml.KNearest_create()

knn.train(trainData, 0, trainLabels)

# Nhan dang
result1, result2, result3, result4 = knn.findNearest(imgTest, 5)

print('Nhan dang la so {}'.format(result2))

cv2.waitKey()
cv2.destroyAllWindows()
