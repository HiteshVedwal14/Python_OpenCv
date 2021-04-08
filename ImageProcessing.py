# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:14:11 2021

@author: HITESH
"""
dir='D:/Python/Deep Learning & Computer Vision, Open CV/Computer-Vision-with-Python/DATA/'
'''

Image Processing

Learn various image processing operations.
Perform image operations such as Smoothing, Blurring, Morphological Operations
Grab properties such as color spaces and histograms.

'''

'''
Color Mapping

HSL Model: Hue, Saturation and Lightness Model
HSV Model: Hue, Saturation and Value Model

'''

#############################################################################################################################
import cv2
import matplotlib.pyplot as plt
import numpy as np
'''
img = cv2.imread(dir+'/00-puppy.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
f_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) 
plt.imshow(img)
plt.imshow(f_img)
'''
#############################################################################################################################


'''
Blending images is done through addWeighted function that uses both images and combines them.
to blend the image formula is 
new_pixel = alpha * pixel_1 + beta * pixel_2 + gamma

'''
'''
img_1 = cv2.imread(dir+'/dog_backpack.png')
img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
img_2 = cv2.imread(dir+'/watermark_no_copy.png')
img_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)

#plt.imshow(img_1)
#lt.imshow(img_2)

# BLENDING IMAGES OF THE SAME SIZE


# Fixiing the sizes of the images to equal
img_1 = cv2.resize(img_1,(1200,1200))
img_2 = cv2.resize(img_2,(1200,1200))


blended = cv2.addWeighted(src1=img_1, alpha=0.9, src2=img_2, beta=0.1, gamma=0)
plt.imshow(blended)
'''
#######################################################################################################
# OVERLAY SMALL IMAGE ON TOP OF A LARGER IMAGE
# Numpy reassignment 
img_1 = cv2.imread(dir+'/dog_backpack.png')
img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
img_2 = cv2.imread(dir+'/watermark_no_copy.png')
img_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)

img_2 = cv2.resize(img_2,(600,600))
'''
small_img = img_2
large_img = img_1

x_offset = 0
y_offset = 0

x_end = x_offset + small_img.shape[1]
y_end = y_offset + small_img.shape[0]

large_img[y_offset:y_end, x_offset:x_end] = small_img
plt.imshow(large_img) 
'''
# BLEND TOGETHER IMAGES OF DIFFERENT SIZES

x_offset = 934 - 600
y_offset = 1401 - 600

rows, cols, channels = img_2.shape

roi = img_1[y_offset:1401, x_offset:934]
#plt.imshow(roi)
img2gray = cv2.cvtColor(img_2, cv2.COLOR_RGB2GRAY)
#plt.imshow(img2gray, cmap='gray')

# Inverse of the color next step
mask_inv = cv2.bitwise_not(img2gray)
#plt.imshow(mask_inv, cmap='gray')

white_background = np.full(img_2.shape, 255, dtype=np.uint8)
bk = cv2.bitwise_or(white_background,white_background,mask=mask_inv)
plt.imshow(bk)

fg = cv2.bitwise_or(img_2, img_2, mask = mask_inv)
plt.imshow(fg)

final_roi = cv2.bitwise_or(roi, fg)
plt.imshow(final_roi)

large_img = img_1
small_img = final_roi

large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img

plt.imshow(large_img)