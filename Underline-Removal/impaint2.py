#Read the comments

import numpy as np
import cv2
import PIL.ImageOps
from PIL import Image
from scipy.misc import toimage


image = Image.open('removedStrikes.png')

mask = np.array(PIL.ImageOps.invert(image))

img = cv2.imread('final.png')

dst = cv2.inpaint(img,mask,3,cv2.INPAINT_NS)
#another algorithm can be implemented using the param: cv2.INPAINT_TELEA
# The value 3 is inpaintRadius : Radius of a circular neighborhood of each point inpainted that is considered by the algorithm.

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
