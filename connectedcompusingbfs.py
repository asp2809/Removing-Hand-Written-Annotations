import cv2
import numpy
import sys

sys.setrecursionlimit(1500000)

height=0
width=0

src = cv2.imread('imgnew.jpg', 0)
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
    
handw=""

for i in range(len(h)):
    if h[i] !=0:
        handw+="Height: " + str(h[i]) + " Width: " + str(w[i]+0.25) + "\n"

f=open("heightandwidth.txt", "w")
f.write(handw)
f.close()