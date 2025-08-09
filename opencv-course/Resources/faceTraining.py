import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Faces\train'
# r'' to treat \ as literal characters



haar_cascade = cv.CascadeClassifier('D:\DanielDesktop\GUC\OpenCV\opencv-course\Section #3 - Faces\haar_face.xml')

# p = []
# for i in os.listdir('D:\\DanielDesktop\\GUC\\OpenCV\\opencv-course\\Resources\\Faces\\train'):
#     p.append(i)

features = []
labels  = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]#crop out the faces
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done ------------------')


features = np.array(features, dtype = 'object')
labels = np.array(labels)

# print(f'Length of the features = {len(features)}')
# print(f'Length of the labels = {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
#train the model on features list and labels list
face_recognizer.train(features, labels)
face_recognizer.save('face_training_done.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)

