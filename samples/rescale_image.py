import cv2 as cv 

img = cv.imread("Photos/cat.jpg")


def rescaleFrame(frame, scale=0.75):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	dimension = (width, height)

	return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

img_rescale = rescaleFrame(img, 3.0)
cv.imshow("Scale", img_rescale)

capture = cv.VideoCapture("Videos/dog.mp4")
try:
	while True:
		isTrue, frame = capture.read()
		frame_rescale = rescaleFrame(frame, 1.2)
		cv.imshow("Dog", frame_rescale)
		
		if cv.waitKey(20) & 0xFF == ord("d"):
			break
except:
	print("Видео завершилось")

capture.release()
cv.destroyAllWindows()

