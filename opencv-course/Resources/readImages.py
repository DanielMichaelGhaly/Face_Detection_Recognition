import cv2 as cv

img = cv.imread('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Photos\cat_large.jpg')

cv.imshow('Cat',img)#name of window and image itself

cv.waitKey(0)#delay in milliseconds before being closed

capture = cv.VideoCapture('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Videos\dog.mp4')#takes either integer so 0 if webcam connected to my computer
#1 if first camera connected to my computer and so on
#or it can take a path to a video

#in videos we must read video frame by frame
while True:
    isTrue, frame = capture.read()#gives the frame and whether it was successfully read or not
    cv.imshow('Dog_Video',frame)

    if cv.waitKey(20) & 0xFF==ord('q'):#time wait for every frame and if letter q is pressed exit
        break
capture.release()#closes video file
cv.destroyAllWindows()