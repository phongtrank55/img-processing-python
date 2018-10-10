import cv2
import numpy as np
import matplotlib.pyplot as plt


trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
color = np.random.randint(0, 2, (25, 1))

red = trainData[color.ravel()==1] #Lấy các điểm trong trainData có color = 1
blue = trainData[color.ravel()==0]

# print(red)

plt.scatter(red[:, 0], red[:, 1], 100, 'red', 's')

plt.scatter(blue[:, 0], blue[:, 1], 100, 'blue', '^')

mem = np.random.randint(0, 100, (1, 2)).astype(np.float32)
# print(mem)
plt.scatter(mem[:, 0], mem[:, 1], 100, 'g', 'o')

#Thuat toan knn
knn = cv2.ml.KNearest_create()
knn.train(trainData, 0, color)

temp, result, neighbor, distance = knn.findNearest(mem, 5) # so sánh 5 hang xom gan nhat va lay theo so dong
print('Ket qua: {}\n' .format(result))
print('Hang xom: {}\n' .format(neighbor))
print('Khoang cach: {}\n' .format(distance))

plt.show()
# print (color)
# print(trainData)




