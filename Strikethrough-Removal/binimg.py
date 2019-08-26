import os, sys
import numpy as np
from PIL import Image
import cv2
from matplotlib import pyplot as plt
from scipy.misc import toimage
from copy import deepcopy

w=0

im_gray = cv2.imread('test1.png',cv2.IMREAD_GRAYSCALE)
thresh, im_bw = cv2.threshold(im_gray, 127, 255, cv2.THRESH_OTSU)
cv2.imwrite('bintest4.png', im_bw)

arr=np.ndarray.tolist(im_bw)
arr1=deepcopy(arr)                                                  #List for the new boundaries image
arr3=[[0 for x in range(len(arr[0]))] for y in range(len(arr))]     #List for the visited vertex, visited=1, not visited=0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i-1>=0 and j-1>=0 and i<len(arr)-1 and j<len(arr[i])-1:
            if arr[i-1][j]==0 and arr[i-1][j-1]==0 and arr[i+1][j]==0 and arr[i+1][j+1]==0 and arr[i-1][j+1]==0 and arr[i+1][j-1]==0 and arr[i][j-1]==0 and arr[i][j+1]==0:
                arr1[i][j]=255

arr2=np.array(arr1)

img = toimage(arr2)
img.save("boundariestest.png")
