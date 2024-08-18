import cv2 as cv
import matplotlib.pyplot as plt 

path = "../Photos/dog.jpg"
img = cv.imread(path)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow("Original", img)
cv.imshow("HSV", hsv)
cv.imshow("LAB", lab)

cv.waitKey(0)

# Image show RGB. OpenCV show images in BGR format.
# plt.imshow(rgb)
# plt.show()