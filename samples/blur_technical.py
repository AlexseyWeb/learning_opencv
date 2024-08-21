import cv2 as cv 

path = "../Photos/dog.jpg"
img = cv.imread(path)


#Average
averaged = cv.blur(img, (6,6))
cv.imshow("Blur", averaged)

gausess_blur = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussus", gausess_blur)

#median blur
median_blur = cv.medianBlur(img, 5)
cv.imshow("Median", median_blur)

#Bilater
bilater = cv.bilateralFilter(img, 5, 45, 34)
cv.imshow("bilater", bilater)

cv.waitKey(0)