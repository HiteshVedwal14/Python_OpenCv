# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:08:43 2021

@author: HITESH
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

dir='D:/Python/Deep Learning & Computer Vision, Open CV/Computer-Vision-with-Python/DATA/'


# =============================================================================
# Histograms
# =============================================================================


dark_horse = cv2.imread(dir+'horse.jpg')                    #Orginal Images
show_horse = cv2.cvtColor(dark_horse, cv2.COLOR_BGR2RGB)    #Converted to RGB for show

rainbow = cv2.imread(dir+'rainbow.jpg')
show_rainbow = cv2.cvtColor(rainbow, cv2.COLOR_BGR2RGB)

blue_bricks = cv2.imread(dir+'bricks.jpg')
show_bricks = cv2.cvtColor(blue_bricks, cv2.COLOR_BGR2RGB)


'''
# OpenCV BGR
hist_values = cv2.calcHist([blue_bricks], channels=[0], mask=None, histSize=[256], ranges=[0,256])
#print(hist_values.shape)

#plt.plot(hist_values)



hist_values = cv2.calcHist([dark_horse], channels=[0], mask=None, histSize=[256], ranges=[0,256])

#plt.plot(hist_values)
'''

img = blue_bricks
img1 = dark_horse
img2 = rainbow
color = ('b', 'g', 'r')
'''
for i,col in enumerate(color):
    hist = cv2.calcHist([img], [i],None, [256], [0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.title('Histogram for Blue Bricks')
'''

'''
for i,col in enumerate(color):
    hist = cv2.calcHist([img1], [i],None, [256], [0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,50])
    plt.ylim([0,500000])
plt.title('Histogram for Dark Horse')
'''
'''
for i,col in enumerate(color):
    hist = cv2.calcHist([img2], [i],None, [256], [0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.title('Histogram for Rainbow')
'''


# =============================================================================
# # Histogram Equalization is a method of contrast adjustment based on the images's histogram
# =============================================================================
#print(img2.shape)

mask = np.zeros(img2.shape[:2],np.uint8)
#plt.imshow(mask,cmap='gray')   

mask[300:400,100:400] = 255

# plt.imshow(mask,cmap='gray')

masked_img = cv2.bitwise_and(img2, img2, mask = mask)
show_mask = cv2.bitwise_and(show_rainbow, show_rainbow, mask=mask)
#plt.imshow(show_mask)

hist_masked_value_red = cv2.calcHist([rainbow], channels=[2], mask=mask, histSize=[256], ranges=[0,256])
hist_value_red = cv2.calcHist([rainbow], channels=[2], mask=None, histSize=[256], ranges=[0,256])
# plt.plot(hist_masked_value_red)
# plt.title('RED HISTOGRAM FOR MASKED RAINBOW')

# plt.plot(hist_value_red)
# plt.title('RED HISTOGRAM FOR NORMAL RAINBOW')

gorilla = cv2.imread(dir+'gorilla.jpg',0)

def display_img(img,cmap=None):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap)

#display_img(gorilla,cmap='gray')
hist_values = cv2.calcHist([gorilla], channels=[0], mask=None, histSize=[256], ranges=[0,256])
#plt.plot(hist_values)

eq_gorilla = cv2.equalizeHist(gorilla)
# display_img(eq_gorilla,cmap='gray')

hist_values1 = cv2.calcHist([eq_gorilla], channels=[0], mask=None, histSize=[256], ranges=[0,256])
# plt.plot(hist_values1)
color_gorilla = cv2.imread(dir+'gorilla.jpg')
show_gorilla = cv2.cvtColor(color_gorilla, cv2.COLOR_BGR2RGB)
#display_img(show_gorilla)

hsv = cv2.cvtColor(color_gorilla, cv2.COLOR_BGR2HSV)
hsv[:,:,2] = cv2.equalizeHist(hsv[:,:,2])
eq_color_gorilla = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
# display_img(eq_color_gorilla)

hist_values3 = cv2.calcHist([eq_color_gorilla], channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.plot(hist_values3)



