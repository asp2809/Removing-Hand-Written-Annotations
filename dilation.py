import cv2
import numpy as np
from PIL import Image
from scipy.misc import toimage
from matplotlib import pyplot as plt

def is_contourbad(c):
    peri = cv2.arcLength(c, True)
    print(peri)
    if peri > 60 and peri < 1000:
        return 1
    return 0

img = cv2.imread("annotationsraw1.png")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image ,cnts, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
mask = np.ones(img.shape[:2], dtype="uint8") * 255

for c in cnts:
    if is_contourbad(c):
        cv2.drawContours(mask,[c],-1,(0),cv2.FILLED)
      

kernel = np.zeros((101,101),np.uint8)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
erosion = cv2.erode(closing,kernel,iterations = 5)
    
plt.imshow(mask)
plt.show()
img = toimage(mask)
# cv2.imshow(img)
img.save("Finalimageraw1.png")