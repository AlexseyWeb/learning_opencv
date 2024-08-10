import cv2 as cv 
""" Samples """


def show_images():
	"""Show all images of folder """
	list_of_images = ["cat.jpg", "funny_dog.jpeg", "white_dog.jpeg"]

	for index, img in enumerate(list_of_images):
		cv.imshow(f"{index}",cv.imread(f"Photos/{img}"))

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








