import cv2 as cv 


path = "../Photos/dog.jpg"
img = cv.imread(path)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
tresholder, tresh = cv.threshold(gray, 95, 255, cv.THRESH_BINARY)
tresholder, tresh_in = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
adaptive_tresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)


cv.imshow("Tresh", tresh)
cv.imshow("Tresh Inversity", tresh_in)
cv.imshow("Adaptive tresh", adaptive_tresh)
cv.waitKey(0)