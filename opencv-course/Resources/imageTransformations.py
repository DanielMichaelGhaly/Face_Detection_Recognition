import cv2 as cv
import numpy as np

img = cv.imread('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Photos\park.jpg')

#Translation
def translate(img, x , y):
    translationMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])#width and height
    return cv.warpAffine(img, translationMatrix, dimensions)
# -x --> left
# -y --> up
# x --> right
# y -->down
translated = translate(img, 100,100)
cv.imshow('Translated', translated)

#Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)#1.0 is scale
    dimensions= (width, height)
    return cv.warpAffine(img, rotMatrix, dimensions)
#angle positive rotates anticlockwise
#angle negative rotates clockwise

#Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#flipping
flip = cv.flip(img, 0)#0(flips it on x axis) , 1(flips it on y axis) , -1(flips it both on x and y axis)

rotated = rotate(img, 45)
cv.imshow('Rotated',rotated)

cv.imshow('flipped', flip)

#cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)
