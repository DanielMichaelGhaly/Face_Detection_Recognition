#Face detection preformed using classifieres
#Classifieres need to be trained with 100s and 1000s of images with and without faces
#Already trained openCV models are haar cascades and more advance core local binary patterns
import cv2 as cv

img = cv.imread('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Photos\group 1.jpg')
cv.imshow('Group1', img)

img2 = cv.imread('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Photos\group 2.jpg')
cv.imshow('Group2', img2)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Group1', gray)
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('D:\DanielDesktop\GUC\OpenCV\opencv-course\Section #3 - Faces\haar_face.xml')
haar_cascade2 = cv.CascadeClassifier('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\haarcascade_smile.xml')

# canny = cv.Canny(gray2, 100,200)
# cv.imshow('Canny', canny)

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
faces_rect2 = haar_cascade2.detectMultiScale(gray2, scaleFactor=1.5, minNeighbors=6)
#minNeighbors is number of neighbors a rectangle should have to be detected as a face
#Increasing minNeighbors increases accuracy of detection
#faces_rect is a list of list of coordinates of faces detected

print(f'Number of faces found = {len(faces_rect)}')
print(f'Number of smiles detected = {len(faces_rect2)}')
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
for (x,y,w,h) in faces_rect2:
    cv.rectangle(img2, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)
cv.imshow('Detected Smiles', img2)

cv.waitKey(0)