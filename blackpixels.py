import cv2
import numpy
import sys
from matplotlib import pyplot as plt

sys.setrecursionlimit(1500000)
src = cv2.imread('imgnew.jpg', 0)

arr=numpy.ndarray.tolist(src)
bp=[]
l1=[]
arr1=[]
for i in range(len(arr)):
    count=0
    for j in range(len(arr[i])):
        if arr[i][j]<=10:
            count+=1
    bp.append(count)
f=open("bpinrow.txt", "w")
for i in range(len(bp)):
    if bp[i]<50:
        l1.append(numpy.ndarray.tolist(src[i:i+1][0]))
    f.write("Row " + str(i) + ": " + str(bp[i]) + "\n")
f.close()
arr1=numpy.array(l1)
plt.imshow(arr1, interpolation='None')
plt.show()



