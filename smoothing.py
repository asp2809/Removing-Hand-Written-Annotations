#Program to smoothen the annotations in annotations.png
import cv2, numpy
from matplotlib import pyplot as plt
from scipy.misc import toimage

src = cv2.imread('annotations1.png', 0)

arr=numpy.ndarray.tolist(src)

j=0
arr3=[[0]*20]*2
i=0
count1=0
while(i<len(arr)):
    j=0
    while(j<len(arr[i])):
        count1=0
        if (i+len(arr3))<=len(arr) and (j+len(arr3[0]))<=len(arr[i]):
            for k in range(len(arr3)):
                for l in range(len(arr3[k])):
                    count1+=arr[i+k][j+l]
            print(count1)
            if count1<7700:
                for k in range(len(arr3)):
                    for l in range(len(arr3[k])):
                        arr[i+k][j+l]=0
            else:
                for k in range(len(arr3)):
                    for l in range(len(arr3[k])):
                        arr[i+k][j+l]=255
        print(len(arr3[k]))
        j+=len(arr3[k])
    print(len(arr3))
    i+=len(arr3)

# for i in range(len(arr)-5):
#     while(j<len(arr[i])):
#         if (j+4)<len(arr[i]):
#             if (arr[i][j])<20 and (arr[i][j+20]<20 or arr[i+1][j+20]<20 or arr[i+2][j+20]<20 or arr[i+3][j+20]<20 or arr[i+4][j+20]<20):
#                 for k in range(20):
#                     arr[i][j+k]=0
#         j+=1

arr1=numpy.array(arr)
plt.imshow(arr1, interpolation='None')
plt.show()

img = toimage(arr1)
img.save("smoothen.png")