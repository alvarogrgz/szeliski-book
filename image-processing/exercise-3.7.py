import numpy as np
import cv2
import matplotlib.pyplot as plt

#TODO
def main():
    img = cv2.imread('../images/lenna.png')
    xyz = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)

    Y = xyz[:,:,2]

    # Easy way: np.histogram(Y.flatten(),256,[0,256]) 
    histogram = np.zeros(256)
    rows, columns = Y.shape
    for row in range(rows):
        for column in range(columns):
            histogram[Y[row,column]] += 1

    # Easy way: cdf = hist.cumsum()
    cumulative = np.zeros(256)
    sum = 0
    for i in range(histogram.size):
        sum += histogram[i]
        cumulative[i] = sum    

    cdf = cumulative/sum
    fig, axs = plt.subplots(2)
    axs[0].plot(range(histogram.size), histogram)
    axs[1].plot(range(cdf.size), cdf)
    plt.show()

    transformation = np.floor(cdf*255)
    Y_transformed = transformation[Y]

    f, axarr = plt.subplots(1,2)
    axarr[0].set_title('Original')
    axarr[0].imshow(Y)
    axarr[1].set_title('Transformed')
    axarr[1].imshow(Y_transformed)
    plt.show()

    xyz_transformed = xyz.copy()
    xyz[:,:,1] = Y_transformed
    img_transformed = cv2.cvtColor(xyz_transformed, cv2.COLOR_XYZ2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    f, axarr = plt.subplots(1,2)
    axarr[0].set_title('Original')
    axarr[0].imshow(img)
    axarr[1].set_title('Transformed')
    axarr[1].imshow(img_transformed)
    plt.show()

    print(img)
    print(img_transformed)

    #cv2.imshow('y', Y)
    #cv2.waitKey(0)
if __name__ == "__main__":
	main()