import cv2 as cv 
import numpy as np

img = cv.imread("../Photos/man.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow("Gradients", lap)
cv.waitKey(0)
