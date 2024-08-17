import cv2 as cv 

img = cv.imread("../Photos/white_dog.jpeg")
cv.imshow("Original", img)

#GRAY IMAGE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Photo", gray)

#BLUR
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

#Edge Cascade
canny = cv.Canny(img, 125, 170)
cv.imshow("Edge Cascade", canny)

#Dilating the image
dilated = cv.dilate(img, (3, 3), iterations=1)
cv.imshow("Dilated", dilated)

#Eroding
eroded = cv.erode(img, (7,7), iterations=3)
cv.imshow("Erode", eroded)

#Resize
resized = cv.resize(img, (50, 50), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

#Cropping
cropped = img[50:255, 150:155]
cv.imshow("Cropped", cropped) 

cv.waitKey(0)