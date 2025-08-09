import cv2 as cv

#lazem t call el method b3d el ketaba bta3tha
def rescaleFrame(frame, scale=0.75):
    #used for Image, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#to rescale specifically for Live Videos
def changeRes(width, height):
    capture.set(3,width)#reference in capture for width is 3
    capture.set(4,height)

# img = cv.imread('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Photos\cat.jpg')
# cv.imshow('Image',img)
# resized_image = rescaleFrame(img, scale = 1.5)
# cv.imshow('resizedImage',resized_image)


capture = cv.VideoCapture('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Videos\dog.mp4')

while True:
    isFrame, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.25)

    cv.imshow('Video',frame)
    cv.imshow('Video_resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break
    
capture.release()
cv.destroyAllWindows()