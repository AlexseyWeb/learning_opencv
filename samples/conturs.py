import cv2 as cv 
import numpy as np 

path = "../Photos/dog.jpg"
img = cv.imread(path)

blank = np.zeros(img.shape, dtype="uint8")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(img , 125, 175)
blur = cv.GaussianBlur(canny, (5, 5), cv.BORDER_DEFAULT)

ret, tresh = cv.threshold(gray, 175, 225, cv.THRESH_BINARY)
cv.imshow("Tresh", tresh)
cv.imshow("Blank", blank)


contours, hiearchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
cv.drawContours(blank, contours, -1, (100,200,100), thickness=1)
cv.imshow("drawBlank",blank)

print(f'{len(contours)} countour(s) is found')
cv.imshow("blur", blur)
cv.imshow("Conturs", canny)

cv.waitKey(0)