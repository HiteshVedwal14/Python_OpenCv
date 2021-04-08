# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 16:42:55 2021

@author: HITESH
"""

########### Blurring and Smoothing

# Gamma Correction

'''
Gamma Correction can be applied to an image to make it appear brighter
or darker depending on the Gamma value chosen.
'''

# Kernel Based Filters

'''
Kernels can be applied over an image to produce a variety of effects

'''


import cv2
import numpy as np
import matplotlib.pyplot as plt

dir='D:/Python/Deep Learning & Computer Vision, Open CV/Computer-Vision-with-Python/DATA/'
'''
def load_img():
    img = cv2.imread(dir+'bricks.jpg').astype(np.float32) / 255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

#load_img()

def display_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img)
    
i = load_img()
#display_img(i)
'''
gamma = 1/4   #Increasing gamma will make the image darker and lower the gamma will make it brighter

#result=np.power(i,gamma)
#display_img(result)
'''
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text='bricks',org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
#display_img(img) 

kernel = np.ones(shape=(5,5),dtype=np.float32)/25

dst = cv2.filter2D(img, -1, kernel)
#display_img(dst)
'''

'''
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text='bricks',org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
print('reset')

blurred = cv2.blur(img,ksize=(10,10))
display_img(blurred)
'''
'''
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text='bricks',org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
print('reset')

blurred_img = cv2.GaussianBlur(img, (5,5), 10)
display_img(blurred_img)
'''
'''

img = cv2.imread(dir+'sammy.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#display_img(img)

noise_img = cv2.imread(dir+'sammy_noise.jpg')
#display_img(noise_img)

median = cv2.medianBlur(noise_img,5)
#display_img(median)

blur = cv2.bilateralFilter(img,9,75,75)
#display_img(blur)

'''

####### Morphological Operators


def load_img():
    blank_img=np.zeros((600,600))
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(blank_img,text='ABCDE', org=(50,300),fontFace=font,fontScale=5,color=(255,255,255),thickness=20)
    return blank_img

#load_img()

def display_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
  
img = load_img()
#display_img(img)

kernel = np.ones((5,5),dtype=np.uint8)
'''
result = cv2.erode(img,kernel,iterations=4)
display_img(result)
'''
'''
white_noise = np.random.randint(low=0,high=2,size=(600,600))
#display_img(white_noise)

white_noise = white_noise * 255
#display_img(white_noise)

noise_img = white_noise + img
#display_img(noise_img)

opening = cv2.morphologyEx(noise_img, cv2.MORPH_OPEN, kernel)
display_img(opening)
'''

'''
black_noise = np.random.randint(low=0,high=2,size=(600,600))
black_noise = black_noise * -255 # will take the values of all the black value to -255
black_noise_img = img + black_noise
black_noise_img[black_noise_img== -255] = 0 # all the values of white to 0

#display_img(black_noise_img)

closing = cv2.morphologyEx(black_noise_img, cv2.MORPH_CLOSE, kernel)
#display_img(closing)
'''
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
display_img(gradient)