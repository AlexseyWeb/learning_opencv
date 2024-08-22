import cv2 as cv 
import numpy as np

path = "../Photos/dog.jpg"
img = cv.imread(path)



blank = np.zeros(img.shape[:2], dtype="uint8")
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 200, 1.0, -1)
mask_two = cv.rectangle(blank, (100, 300), (img.shape[1] // 2, img.shape[0] // 3),  1.0, -2 )

masked = cv.bitwise_and(img, img, mask=mask_two)


cv.imshow("Masked Text", masked)
cv.waitKey(0)