import cv2 as cv 

img = cv.imread("../Photos/man.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
haar_cascade = cv.CascadeClassifier("har_detector.xml")
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f"Number of faces = {len(face_rect)}")
for (x, y, w, h) in face_rect:
    cv.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("Face detector", img)

cv.waitKey(0)