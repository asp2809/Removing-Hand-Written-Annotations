import os, sys
import numpy as np
from PIL import Image
import cv2
from matplotlib import pyplot as plt
from scipy.misc import toimage
from copy import deepcopy

seedlength=int(input("Enter the seed length: "))
seed = [0]*seedlength;

strikethroughsset = set([])

im_gray = cv2.imread('final.png',cv2.IMREAD_GRAYSCALE)
thresh, im_bw = cv2.threshold(im_gray, 127, 255, cv2.THRESH_OTSU)
cv2.imwrite('binfinl.png', im_bw)


img = np.ndarray.tolist(im_bw)

# Looping through the complete image and then checking the threshold of the black pixels to the seed and then checking if the threshold is greater than 70% of the total length

for i in range(len(img)):
    for j in range(len(img[i])):
        count=0
        for k in range(len(seed)):
            if j+k<len(img[i]):
                if seed[k]==img[i][j+k]:
                    count+=1
        if(count>=(0.7*len(seed))):
            for k in range(len(seed)):
                if j+k<len(img[i]):
                    if seed[k]==img[i][j+k]:
                        strikethroughsset.add((i,j+k))

# Preparing an image with all the black pixels counted by the above Looping

newimgarray = [[1 for i in range(len(img[0]))] for j in range(len(img))]

for val in strikethroughsset:
    newimgarray[val[0]][val[1]]=0

newimg=np.array(newimgarray)
plt.imshow(newimg, interpolation="None")
plt.show()
newimg1=toimage(newimg)
newimg1.save("removedStrikes.png")
