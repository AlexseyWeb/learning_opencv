import cv2 as cv 
""" Samples """


def rescale(frame, scale=0.73):
	""" Function for scale image and video """
	width = int(frame.shape[1] * scale) 
	height = int(frame.shape[0] * scale)
	dimension = (width, height)

	return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def show_images(scale):
	"""Show all images of folder """
	list_of_images = ["cat.jpg", "funny_dog.jpeg", "white_dog.jpeg"]

	for index, img in enumerate(list_of_images):
		photo = cv.imread(f"Photos/{img}")
		img_scale = rescale(photo, scale=scale)
		cv.imshow(f"{index}", img_scale)

	cv.waitKey(0)

def show_videos():
	"""Show videos of folder """
	capture = cv.VideoCapture("Videos/dog.mp4")
	while True:
		_, frame = capture.read()
		cv.imshow("Video", frame)
		if cv.waitKey(20) & 0xFF == ord('d'):
			break

	capture.release()
	cv.destroyAllWindows()


show_images(2.8)







