from fastai.vision import *
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('D:\DanielDesktop\GUC\OpenCV\opencv-course\Resources\Photos\lady.jpg')

h, w = img.shape[:2]

plt.figure(figsize=(w/30,h/30))
plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))

print(cv.__version__)

cv.waitKey(0)