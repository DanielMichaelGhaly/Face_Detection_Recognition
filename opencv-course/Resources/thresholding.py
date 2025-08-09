import cv2 as cv

img = cv.imread('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Photos\cats 2.jpg')
cv.imshow("image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Simple Thresholding (thresholding is converting pixels of pic into either black or white)
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
#if value of pixel greater than 150 then threshold it to 255
cv.imshow("Simple thresholded", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
#less than 150 to 255
cv.imshow('Simple Inverse Threshold', thresh_inv)

# Adaptive Thresholding(to find optimal threshold value)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11, 3)
#11 is kernel size, 3 is C value that is subtracted from mean to get threshold and it is increase it gives more sharpened photo
cv.imshow("Adaptive Threshold", adaptive_thresh)

cv.waitKey(0)