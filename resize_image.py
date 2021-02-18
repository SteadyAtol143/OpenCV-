import cv2 as cv
import numpy as np

Image = cv.imread("Resources/image.jpg")

scale_percent = 60
width = int(Image.shape[1] * scale_percent / 100)
height = int(Image.shape[0] * scale_percent / 100)
dim = (width,height)
resized = cv.resize(Image,dim)

cv.imshow("Image Resized", resized)

cv.waitKey(0)
