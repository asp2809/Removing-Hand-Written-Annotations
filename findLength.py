import cv2 
import numpy
import sys
from PIL import Image
from matplotlib import pyplot 
from scipy.misc import toimage

sys.setrecursionlimit(150000000)

src = cv2.imread('bintest4.png', 0)
arr=numpy.ndarray.tolist(src)
arrnew=[[255 for x in range(len(arr[0]))] for y in range(len(arr))]

length=0
maxi=0
maxj=0

def findLength(i, j):
    global length
    global maxi
    global maxj
    flag=0
    if j<(len(arr[i])-1) and arr[i][j+1]==0:
        length+=1
        j+=1
        flag=1
    elif i<(len(arr)-1) and j<(len(arr[i])-1) and arr[i+1][j+1]==0:
        length+=1
        j+=1
        i+=1
        flag=1
    if j<(len(arr[i])-1) and i>0 and arr[i-1][j+1]==0:
        length+=1
        j+=1
        i-=1
        flag=1
    if(flag==1):
        findLength(i, j)
    if(flag==0):
        # print(i, j)
        maxi=i
        maxj=j
img = Image.open("bintest4.png") 
width=len(arr[0])
height=len(arr)
image=Image.new('RGB', (width, height), (255, 255, 255))
tempi=0
tempj=0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if(arr[i][j]==0):
            maxi=0
            maxj=0
            tempi=i
            tempj=j
            length=0
            findLength(i, j)
            # print(maxi, maxj)
            if(length>40):
                print(maxi, maxj)
                border_box = (tempj-53, tempi-50, maxj+53, maxi+50)
                img2=img.crop(border_box)
                image.paste(img2, border_box)
                
            

image.save("final.png")


