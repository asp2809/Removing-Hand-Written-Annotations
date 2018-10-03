import cv2
import numpy
import sys
from matplotlib import pyplot as plt
from scipy.misc import toimage

sys.setrecursionlimit(1500000)

src = cv2.imread('binimage.png', 0)
arr=numpy.ndarray.tolist(src)

seed=[0]*8
seedcount=0
seedcoord=[]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]==0 and (j+7)<len(arr[i]):
            flag=1
            for k in range(len(seed)):
                if arr[i][j+k]!=seed[k]:
                    flag=0
            if flag==1:
                seedcount+=1
                seedcoord.append([i, j])
            j+=7

print(seedcount)
for y in seedcoord:
    print(str(y[0]) + "\t" + str(y[1]))
countleft=0
countright=0


leftseedext=[]
def countheightleft(i, j):
    global countleft
    if arr[i][j-1]==0 and j>0:
        j-=1
        countheightleft(i, j)
    elif arr[i-1][j-1]==0 and i>0 and j>0:
        if countleft<3:
            countleft+=1
        else:
            leftseedext.append([i, j])
            return
        i-=1
        j-=1
        countheightleft(i, j)
    elif arr[i+1][j-1]==0 and i<(len(arr)-1) and j>0:
        if countleft<3:
            countleft+=1
        else:
            leftseedext.append([i, j])
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
        j-=1
        countheightright(i, j)
    elif arr[i+1][j+1]==0 and i<(len(arr)-1) and j<(len(arr[i])-1):
        if countright<3:
            countright+=1
        else:
            rightseedext.append([i, j])
            return 
        i+=1
        j+=1
        countheightright(i, j)
    elif arr[i-1][j+1]==0 and i<(len(arr)-1) and j>0:
        if countright<3:
            countright+=1
        else:
            rightseedext.append([i, j])
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
    countheightleft(x[0], x[1])
    countheightright(x[0]+7, x[1]+7)

print("Seed Coordinate\t\tLeft Extension\t\tRight Extension")
for x in range(len(seedcoord)):
    print(str(seedcoord[x]) + "\t\t" + str(leftseedext[x]) + "\t\t" + str(rightseedext[x]))