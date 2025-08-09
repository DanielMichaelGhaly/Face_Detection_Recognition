import cv2 as cv
import numpy as np

img = cv.imread('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Photos\cats.jpg')
cv.imshow('Image', img)

gray =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F) # data depth
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel calculate gradient in both x and y directions
sobelx = cv.Sobel(gray, cv.CV_64F, 1 , 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0 , 1)
combine = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel x', sobelx)
cv.imshow('Sobel y', sobely)
cv.imshow('CombinedSobel', combine)

#Canny uses sobel method in its method(Canny is used most and then sobel)
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)
