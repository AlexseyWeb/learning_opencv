import cv2 as cv 
import numpy as np 

img = cv.imread("../Photos/man.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 7, 0.05, 25)
corners = np.float32(corners)

for item in corners:
    x, y = item[0]
    cv.circle(img,  (int(x), int(y)), 10, (0, 0, 255), -1)

cv.imshow("Top", img)
cv.waitKey(0)
