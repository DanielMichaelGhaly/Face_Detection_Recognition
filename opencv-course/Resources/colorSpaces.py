import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Photos\park.jpg')
cv.imshow('Boston', img)

#normal libraries use RGB colors so inverted colors
# plt.imshow(img)
# plt.show()

#must convert any color scale to BGR and then convert to any other color scale

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
#so now plt.imshow(rgb)gives the right colors

cv.waitKey(0)
