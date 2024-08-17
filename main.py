import cv2 as cv 

img = cv.imread("Photos/cat.jpg")
canny = cv.Canny(img, 200, 200)
resize_canny = cv.resize(canny, (500, 500), interpolation=cv.INTER_LINEAR)
cv.imshow("Title", resize_canny)


cv.waitKey(0)