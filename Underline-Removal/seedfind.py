import cv2
import numpy
import sys
from PIL import Image
from matplotlib import pyplot as plt
from scipy.misc import toimage
from copy import deepcopy

sys.setrecursionlimit(1500000)

src = cv2.imread('boundaries.png', 0)
arr=numpy.ndarray.tolist(src)
arrnew=[[255 for x in range(len(arr[0]))] for y in range(len(arr))]


seed=[0]*8
seedcount=0
seedcoord=[]

for i in range(len(arr)):
    j=0
    while(j<len(arr[i])):
        # print(i, j)
        if arr[i][j]==0 and (j+7)<len(arr[i]):
            flag=1
            for k in range(len(seed)):
                if arr[i][j+k]!=seed[k]:
                    flag=0
            if flag==1:
                seedcount+=1
                seedcoord.append([i, j])
                j+=7
        j+=1

print(seedcoord)
countleft=0
countright=0


leftseedext=[]
def countheightleft(i, j):
    global countleft
    if arr[i][j-1]==0 and j>0:
        arrnew[i][j-1]=0
        j-=1
        countheightleft(i, j)
    elif arr[i-1][j-1]==0 and i>0 and j>0:
        if countleft<3:
            arrnew[i-1][j-1]=0
            countleft+=1
        else:
            # leftseedext.append([i, j])
            return
        i-=1
        j-=1
        countheightleft(i, j)
    elif arr[i+1][j-1]==0 and i<(len(arr)-1) and j>0:
        if countleft<3:
            arrnew[i+1][j-1]=0
            countleft+=1
        else:
            # leftseedext.append([i, j])
            return
        i+=1
        j-=1
        countheightleft(i, j)
    else:
        leftseedext.append([i, j])

rightseedext=[]
def countheightright(i, j):
    global countright
    if arr[i][j+1]==0 and j<(len(arr[i])-1):
        arrnew[i][j-1]=0
        j-=1
        countheightright(i, j)
    elif arr[i+1][j+1]==0 and i<(len(arr)-1) and j<(len(arr[i])-1):
        if countright<3:
            arrnew[i-1][j-1]=0
            countright+=1
        else:
            # rightseedext.append([i, j])
            return 
        i+=1
        j+=1
        countheightright(i, j)
    elif arr[i-1][j+1]==0 and i<(len(arr)-1) and j>0:
        if countright<3:
            arrnew[i+1][j-1]=0
            countright+=1
        else:
            # rightseedext.append([i, j])
            return 
        i-=1
        j+=1
        countheightright(i, j)
    else:
        leftseedext.append([i, j])
validext=[]
for x in seedcoord:
    countleft=0
    countright=0
    for i in range(8):
        arrnew[x[0]][x[1]+ i]=0
    countheightleft(x[0], x[1])
    countheightright(x[0], x[1]+7)

arr2=numpy.array(arrnew)
print(arr2)
plt.imshow(arr2)
plt.show()
img = toimage(arr2)
img.save("annotations2.png")