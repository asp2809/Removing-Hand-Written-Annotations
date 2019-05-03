import cv2
import numpy as np
import sys
from PIL import Image
from matplotlib import pyplot as plt
from scipy.misc import toimage

sys.setrecursionlimit(1500000)


im_gray = cv2.imread('final.png',cv2.IMREAD_GRAYSCALE)
thresh, im_bw = cv2.threshold(im_gray, 127, 255, cv2.THRESH_OTSU)
cv2.imwrite('binfinl.png', im_bw)


img = np.ndarray.tolist(im_bw)

w=len(img[0])
h=2

bar = [[0 for x in range(w)] for y in range(h)]

#Checking for the black pixels in the particular line and considering it a line only if the number of black pixels are greater than a threshold

for i in range(len(img)):
    if (i+h)<len(img):
        count=0
        for j in range(len(bar)):
            for k in range(len(bar[j])):
                if (img[i+j][k])==bar[j][k]:
                    count+=1
        if count>850:
            for j in range(len(bar)):
                for k in range(len(bar[j])):
                    img[i+j][k]=255

arr2 = np.array(img)
print(arr2)
imgnew = toimage(arr2)
imgnew.save("removedLines.png")
plt.imshow(arr2, interpolation='None')
plt.show()
