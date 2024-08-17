import cv2 as cv 

img = cv.imread("../Photos/funny_dog.jpeg")
cv.imshow("Original", img)

#GRAY IMAGE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Photo", gray)

#BLUR
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)



cv.waitKey(0)