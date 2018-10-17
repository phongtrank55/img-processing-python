import cv2
import numpy as  np


img = cv2.imread('Image/darkbook.png')

result, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
result2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
#Ap dung bo loc
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

result3, otsu = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# print(cv2.THRESH_OTSU)

cv2.imshow('ORIGINAL', img)
cv2.imshow('Threshold', threshold)
cv2.imshow('Threshold 2', threshold2)
cv2.imshow('Otsu', otsu)
cv2.imshow('Gaus', gaus)
cv2.waitKey()
cv2.destroyAllWindows()
