import numpy as np
import cv2
import PIL.ImageOps
from PIL import Image
from scipy.misc import toimage


image = Image.open('removedStrikes.png')

mask = np.array(PIL.ImageOps.invert(image))

img = cv2.imread('final.png')
#the below will be the mask image which will contain only the strikethroughs, the one you will extract
# mask = cv2.imread('removedStrikes.png',0)

dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
#another algorithm can be implemented using the param: cv2.INPAINT_NS

cv2.imshow('dst',dst)
imgnew = toimage(dst)
imgnew.save("inpaint.png")
cv2.waitKey(0)
cv2.destroyAllWindows()
