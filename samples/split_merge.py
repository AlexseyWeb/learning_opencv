import cv2 as cv 
import numpy as np

path = "../Photos/dog.jpg"
img = cv.imread(path)
blank = np.zeros(img.shape[:2], dtype="uint8")

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# cv.imshow("Blue", b)
# cv.imshow("Green", g)
# cv.imshow("Red", r)
cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)


#Merge
merged = cv.merge([b, g, r])
cv.imshow("Merge", merged)

cv.waitKey(0)