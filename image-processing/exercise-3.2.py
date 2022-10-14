import numpy as np
import cv2

#TODO
def main():
    img = np.fromfile('../images/image.rw2', dtype=np.uint8)
    print(img.shape)

if __name__ == "__main__":
	main()