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

#Rotation
def rotation(img, angle, rPoint=None):
    (height, width) = img.shape[:2]
    if rPoint is None:
        rPoint = (width // 2, height // 2)
    
    rotMath = cv.getRotationMatrix2D(rPoint, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMath, dimension)

rotated = rotation(img, 90)
    

cv.imshow("Dog", rotated)
cv.waitKey(0)