import matplotlib.pyplot as plt
import numpy as np
import cv2;

np.random.seed(19680801)

N = 50

x = np.random.rand(N)
y = np.random.rand(N)
color = np.random.rand(N)
# print(color)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

# print(len(area))
plt.scatter(x, y, area, color, 'o')
plt.show()

# cv2.waitKey()
# plt.ion()