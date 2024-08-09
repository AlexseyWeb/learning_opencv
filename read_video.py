import cv2 as cv

capture = cv.VideoCapture("Videos/dog.mp4")
try:
	while True:
		isTrue, frame = capture.read()
		cv.imshow("Dog", frame)
		
		if cv.waitKey(20) & 0xFF == ord("d"):
			break
except:
	print("Видео завершилось")

capture.release()
cv.destroyAllWindows()


