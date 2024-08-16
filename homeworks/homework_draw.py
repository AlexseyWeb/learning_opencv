import cv2 as cv 
import numpy as np 

img = cv.imread("Photos/cat.jpg")
blank = np.zeros((400, 400, 3), np.uint8)
font = cv.FONT_HERSHEY_SIMPLEX

cv.line(blank, (200, 200), (100, 100), (255, 0, 255), thickness=1)


for i in range(0, 150):
	cv.line(blank, (i, i + 10), (100, i), (255, 0, 255), thickness=1)
	cv.rectangle(blank, (i + 10, i), (i, 100), (0, 255, 0), 3)


cv.putText(blank, "OpenCV", (120, 80), font, 2, (255, 255, 255), 2, cv.LINE_AA)
cv.circle(blank,(200, 200), 20, (0, 0, 255), -1) 
cv.imshow("Draw", blank)

cv.putText(img, "Cat", (img.shape[1] // 2, img.shape[0] // 2), font, 2, (0, 0, 33), 2, cv.LINE_AA)
cv.imshow("Lable", img)

cv.waitKey(0)