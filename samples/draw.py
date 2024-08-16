import cv2 as cv 
import numpy as np 

"""Drawing on photo and video"""

blank_img = np.zeros((400, 340, 3), dtype="uint8")
cv.imshow("Blank", blank_img)

blank_img[200:300, 100:200] =  118, 65, 138
cv.imshow("Color", blank_img)

#draw circle
cv.circle(blank_img, (blank_img.shape[1] // 2, blank_img.shape[0]//2), 40, (0, 255, 0), thickness=-1)
cv.imshow("Circle", blank_img)

#draw Line 
cv.line(blank_img, (100, 100), (blank_img.shape[1]//2, blank_img.shape[0]//2), (255, 0, 244), thickness=3)
cv.imshow("Line", blank_img)

#draw Rectangle
cv.rectangle(blank_img, (100, 200), (blank_img.shape[1]//2, blank_img.shape[0]//2), (0, 123, 231), thickness=4)
cv.imshow("Rectangle", blank_img)

#draw Text
cv.putText(blank_img, "OpenCV", (100, 100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,244,123))
cv.imshow("Text", blank_img)
cv.waitKey(0)