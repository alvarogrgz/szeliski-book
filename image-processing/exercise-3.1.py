import numpy as np
import cv2

before_window = 'Before gamma'
after_window = 'After gamma'

def task_1(image: np.ndarray):

	cv2.namedWindow(before_window)
	cv2.createTrackbar('Blue', before_window, 10, 100, on_change)
	cv2.createTrackbar('Green', before_window, 10, 100, on_change)
	cv2.createTrackbar('Red', before_window, 10, 100, on_change)

	cv2.namedWindow(after_window)
	cv2.createTrackbar('Blue', after_window, 10, 100, on_change)
	cv2.createTrackbar('Green', after_window, 10, 100, on_change)
	cv2.createTrackbar('Red', after_window, 10, 100, on_change)
	while(1):

		b = cv2.getTrackbarPos('Blue', before_window)
		g = cv2.getTrackbarPos('Green', before_window)
		r = cv2.getTrackbarPos('Red', before_window)

		before_image = image.copy()
		before_image = adjust_gamma(before_image)
		before_image[:,:,0] = cv2.multiply(before_image[:,:,0], b/10)
		before_image[:,:,1] = cv2.multiply(before_image[:,:,1], g/10)
		before_image[:,:,2] = cv2.multiply(before_image[:,:,2], r/10)

		b = cv2.getTrackbarPos('Blue', after_window)
		g = cv2.getTrackbarPos('Green', after_window)
		r = cv2.getTrackbarPos('Red', after_window)

		after_image = image.copy()
		after_image[:,:,0] = cv2.multiply(after_image[:,:,0], b/10)
		after_image[:,:,1] = cv2.multiply(after_image[:,:,1], g/10)
		after_image[:,:,2] = cv2.multiply(after_image[:,:,2], r/10)
		after_image = adjust_gamma(after_image)

		cv2.imshow(before_window, before_image)	
		cv2.imshow(after_window, after_image)	

		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			break

	cv2.destroyAllWindows()
	return None

def adjust_gamma(image, gamma=2.2):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

def on_change(value):
	pass

def main():
	img = cv2.imread('../images/lenna.png')
	task_1(img)

if __name__ == "__main__":
	main()