""" Image Transformations example"""
import cv2 as cv 
import numpy as np

path = "../Photos/dog.jpg"
img = cv.imread(path)

#Translation
def translate(img, x, y):
    # -x -> Left
    # -y -> Up
    # x -> Right
    # y -> Down

    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, -100, -100)
    

cv.imshow("Dog", translated)
cv.waitKey(0)