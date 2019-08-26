import cv2
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np   

img = cv2.imread("binrawimage1.png")
img1=np.ndarray.tolist(img)
for i in range(len(img1)):
    for j in range(len(img1[i])):
        if img1[i][j]==[255,255,255]:
            img1[i][j]=[0,0,0]
        elif img1[i][j]==[0,0,0]:
            img1[i][j]=[255,255,255]
img=np.array(img1)
plt.imshow(img)
plt.show()
# mimg = cv2.imread("abhoja.png")
# mimg1=np.ndarray.tolist(mimg)
# for i in range(len(mimg1)):
#     for j in range(len(mimg1[i])):
#         if mimg1[i][j]==[255,255,255]:
#             mimg1[i][j]=[0,0,0]
#         elif mimg1[i][j]==[0,0,0]:
#             mimg1[i][j]=[255,255,255]
# mimg=np.array(mimg1)
# plt.imshow(mimg)
# plt.show()
simg = cv2.imread("annotationsraw1.png")
simg1=np.ndarray.tolist(simg)
for i in range(len(simg1)):
    for j in range(len(simg1[i])):
        if simg1[i][j]==[255,255,255]:
            simg1[i][j]=[0,0,0]
        elif simg1[i][j]==[0,0,0]:
            simg1[i][j]=[255,255,255]
simg=np.array(simg1)
plt.imshow(simg)
plt.show()

fimg = img - simg
fimg1=np.ndarray.tolist(fimg)
for i in range(len(fimg1)):
    for j in range(len(fimg1[i])):
        if fimg1[i][j]==[255,255,255]:
            fimg1[i][j]=[0,0,0]
        elif fimg1[i][j]==[0,0,0]:
            fimg1[i][j]=[255,255,255]
fimg=np.array(fimg1)
plt.imshow(fimg)
plt.show()
