import cv2 as cv

img = cv.imread('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Photos\park.jpg')

cv.imshow('Image', img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)#has to be odd number and as it increase gives more blurred image
cv.imshow('Blurred', blur)

#Edge Cascade (To find edges of photo)
canny = cv.Canny(img, 125, 175)
canny2 = cv.Canny(blur, 0, 175)
cv.imshow('Canny Edges',canny)
cv.imshow('Blurred Canny Edges', canny2)

#dilating an image
#dilation adds pixels to boundaries of objects in an image while erosion removes pixels on object boundaries

dilated = cv.dilate(canny, (3,3), iterations = 1)
cv.imshow('Dilated Image', dilated)

#Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded Image', eroded)

#Resizing an image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
#cubic is smallest of them but gives the highest quality and also INTER_linear used if enlarging but if shrinking use inter_area

#cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)