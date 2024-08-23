import cv2 as cv 
import matplotlib.pyplot as plt

img = cv.imread("../Photos/dog.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 255])

#draw histogram
plt.figure()
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()


cv.waitKey(0)