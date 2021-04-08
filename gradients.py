# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:21:47 2021

@author: HITESH
"""


#### GRADIENTS


'''
An Image gradient is a directional change in the intensity or color in an image.

Sobel-Feldman Operators

Normalized x-gradient from Sobel Operator will see the changes in vertical edges 
Normalized y-gradient from Sobel Operator will see the changes in horizontal edges
Normalized gradient magnitude from Sobel Operator will see the changes in both vertical-horizontal edges


Operator uses two 3X3 kernels which are convolved with the original image to calculate approximations of the
derivatives- one for horizontal changes, and one for vertical
'''


import cv2
import numpy as np
import matplotlib.pyplot as plt

dir='D:/Python/Deep Learning & Computer Vision, Open CV/Computer-Vision-with-Python/DATA/'

'''
def load_img():
    blank_img=np.zeros((600,600))
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(blank_img,text='ABCDE', org=(50,300),fontFace=font,fontScale=5,color=(255,255,255),thickness=20)
    return blank_img
'''

def display_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')

img = cv2.imread(dir+'sudoku.jpg',0)
#display_img(img) 

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
#display_img(sobelx)

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
#display_img(sobely)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
#display_img(laplacian)

blended = cv2.addWeighted(src1=sobelx, alpha=0.5, src2=sobely, beta=0.5, gamma=0)
#display_img(blended)

ret, th1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
#display_img(th1)

kernel = np.ones((4,4),np.uint8)
gradient = cv2.morphologyEx(blended, cv2.MORPH_GRADIENT, kernel)
#ret, th1 = cv2.threshold(blended, 100, 255, cv2.THRESH_BINARY)
display_img(gradient)

'''
white_noise = np.random.randint(low=0,high=2,size=(1024,962))
white_noise = white_noise * 255

noise_img = white_noise + gradient

opening = cv2.morphologyEx(noise_img, cv2.MORPH_OPEN, kernel)
#display_img(opening)
'''
black_noise = np.random.randint(low=0,high=2,size=(1024,962))
black_noise = black_noise * -255 # will take the values of all the black value to -255
black_noise_img = gradient + black_noise
black_noise_img[black_noise_img== -255] = 0 # all the values of white to 0

#display_img(black_noise_img)

closing = cv2.morphologyEx(black_noise_img, cv2.MORPH_CLOSE, kernel)
#display_img(closing)

