import cv2
import numpy
import sys
from matplotlib import pyplot as plt
from scipy.misc import toimage

sys.setrecursionlimit(1500000)

height=0
width=0

src = cv2.imread('annotations.png', 0)
arr=numpy.ndarray.tolist(src)

pixel_dim=0.25
arr1=[]
for i in arr:
    arr2=[]
    for j in i:
        arr2.append(0)
    arr1.append(arr2)
h=[]
w=[]
def search(i, j):
    global height
    global width
    arr1[i][j]=1
    if j<len(arr[i])-1 and arr[i][j+1]<=10 and arr1[i][j+1]==0:
        height= height + pixel_dim
        search(i, j+1)
    if j>0 and arr[i][j-1]<=10 and arr1[i][j-1]==0:
        height=height + pixel_dim
        search(i, j-1)
    if i<len(arr)-1 and arr[i+1][j]<=10 and arr1[i+1][j]==0:
        width=width + pixel_dim
        search(i+1, j)
    if i>0 and arr[i-1][j]<=10 and arr1[i-1][j]==0:
        width=width + pixel_dim
        search(i-1, j)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]<=10 and arr1[i][j] == 0:
            height=0
            width=0
            search(i, j)
            h.append(height)
            w.append(width)
            print(h[len(h)-1])
            print(w[len(h)-1]+0.25)
            if h[len(h)-1]<20.0 or w[len(h)-1]>1.5:
                l=h[len(h)-1]/0.25
                r=(w[len(h)-1]/0.25)+1
                if i+l<len(arr) and j+r<len(arr[i]):
                    for k in range(int(l)):
                        for z in range(int(r)):
                            arr[i+k][j+z]=255
    
handw=""

for i in range(len(h)):
    if h[i] !=0:
        handw+="Height: " + str(h[i]) + " Width: " + str(w[i]+0.25) + "\n"

f=open("heightandwidth.txt", "w")
f.write(handw)
f.close()

arr2=numpy.array(arr)
plt.imshow(arr2, interpolation='None')
plt.show()

img = toimage(arr2)
img.save("annotations1.png")