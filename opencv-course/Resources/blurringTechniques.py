import cv2 as cv

img = cv.imread('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Photos\cats.jpg')

cv.imshow('Image', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow("Average Blur",average)

#Gaussian Blur is more realistic(gives less blur)
gauss = cv.GaussianBlur(img, (3,3), 0) # 0 is standard deviation in x direction
cv.imshow('Gauss', gauss)

#Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25) # 5 is diameter and 15 is sigmaColor to be taken in consideration
#15 how far from matrix is affected by the pixels
cv.imshow("Bilateral",bilateral)

cv.waitKey(0)