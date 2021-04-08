# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:17:49 2021

@author: HITESH
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

dir='D:/Python/Deep Learning & Computer Vision, Open CV/Computer-Vision-with-Python/DATA/'
'''
img = cv2.imread(dir+'rainbow.jpg',0)

#plt.imshow(img,cmap='gray')

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) #THRESH_BINARY_INV will do the opposite of THRESH_BINARY

print(ret)


plt.imshow(thresh1,cmap='gray')



ret1,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
plt.imshow(thresh2,cmap='gray')
'''


'''
THRESH_BINARY
THRESH_BINARY_INV
THRESH_TRUNC
THRESH_TOZERO
THRESH_TOZERO_INV
THRESH_MASK
THRESH_OTSU
THRESH_TRIANGLE
'''


img1 = cv2.imread(dir+'crossword.jpg',0)
#plt.imshow(img1,cmap='gray')

def show_pic(image):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(image, cmap = 'gray')
    
#show_pic(img1)

ret, thresh1 = cv2.threshold(img1,200,255,cv2.THRESH_BINARY)
#show_pic(thresh1)

th2 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 8)
show_pic(th2)

blended = cv2.addWeighted(src1=thresh1, alpha=0.6, src2=th2, beta=0.4, gamma=0)
show_pic(blended)


