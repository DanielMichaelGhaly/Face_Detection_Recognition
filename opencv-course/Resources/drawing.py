import cv2 as cv
import numpy as np

#blank image to draw on

blank = np.zeros((500,500,3), dtype='uint8') #3 is number of color channels
# cv.imshow('Blank',blank)

# blank[:] = 0,255,0 # : means all window
# cv.imshow('Green', blank)
# blank[:] = 255,0,0 
# cv.imshow('Blue', blank)
# blank[:] = 0,0,255
# cv.imshow('Red', blank)
# blank[300:400 , 350:450] = 0,0,255 #width and height on x and y axis
# cv.imshow('Red Rectangle', blank)

#alternative is (blank.shape[1]//2,blank.shape[0]//2)
cv.rectangle(blank, (300,300), (400,400),(0,255,0),thickness=2)#only outline
cv.rectangle(blank, (50,50), (250,250),(0,255,0),thickness=cv.FILLED)#fill it or alternatively thickness=-1
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2),40, (0,0,255),thickness=-1)#40 pixels radius
cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,255,255),thickness=3)

#to write text
cv.putText(blank, 'Hello World', (200,255), cv.FONT_HERSHEY_TRIPLEX, 1.25, (255,255,255), thickness=3)#255,255 is origin

cv.imshow('Green Rectangle', blank)

cv.waitKey(0)