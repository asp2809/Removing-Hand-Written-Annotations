import cv2
import numpy
import sys
from scipy.misc import toimage
from matplotlib import pyplot as plt
from PIL import Image
sys.setrecursionlimit(1500000)
src = cv2.imread('imgbin.jpg', 0)

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
<<<<<<< HEAD
plt.Axes.set_facecolor(color="#fff")
plt.imshow(arr1, interpolation='None')
plt.show()
=======

plt.imshow(arr1, interpolation='None')
plt.show()
plt.savefig("imageblk.jpg",dpi = 500)


img = toimage(arr1)
img.save("annotations.png")
>>>>>>> 459f6255daaac076562e04a81142950517c7188d
