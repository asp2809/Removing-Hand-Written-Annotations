import cv2
import sys
from PIL import Image
from scipy.misc import imsave
import numpy 
# from matplotlib import pyplot as plt

def binarize_image(img,nimg):
    imgf = cv2.imread(img,0)
    ret, thresh = cv2.threshold(imgf, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    image = numpy.array(imgf)
    cv2.GaussianBlur(image,(5,5),0)
    image = binarize_array(image,ret)

    imsave(nimg, image)


def binarize_array(numpy_array, threshold):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array


if __name__ == "__main__":
    binarize_image(sys.argv[1], sys.argv[2])

 