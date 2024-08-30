import cv2 as cv 

img = cv.imread("../Photos/animals.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


cv.imshow("Animals", gray)
cv.waitKey(0)