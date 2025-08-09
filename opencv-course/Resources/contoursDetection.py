import cv2 as cv
import numpy as np

img = cv.imread('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Photos\cats.jpg')

#contours are like edges whether lines or curves
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Contours', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("Blurred", blur)

# canny = cv.Canny(blur, 125,175)
# cv.imshow('Canny', canny)

#another way instead of canny
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
#any pixel density less than 125 is blackened and above is white or 255
cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#either cv.RETR_TREE if want all contours that are in a hierarchy
#or cv.RETR_EXTERNAL for only external contours
#or RETR_LIST for all contours in the image
#contours is a python list of all contours coordinates in the image
#hierachies tells for example if a square is inside a circle
#cv.CHAIN_APPROX_NONE
#cv.CHAIN_APPROX_SIMPLE if for example there is a line it compresses it into its starting and end points

cv.drawContours(blank, contours, -1, (0,0,255),1)#-1 specifying you want to draw them all and 2 is thickness
print(f'{len(contours)} countour(s) found!')
cv.imshow("ContourImage", blank)

#use canny better than thresold way

cv.waitKey(0)