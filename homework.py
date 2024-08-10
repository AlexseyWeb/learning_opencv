import cv2 as cv 


list_of_images = ["cat.jpg", "funny_dog.jpeg", "white_dog.jpeg"]

for index, img in enumerate(list_of_images):
	cv.imshow(f"{index}",cv.imread(f"Photos/{img}"))


cv.waitKey(0)
