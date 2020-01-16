
import cv2

def preprocess():

	img_name = 'test.tif'
	im = cv2.imread(img_name)
	gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)

	cv2.imwrite("pre.tif",thresh)

	return "okay"


