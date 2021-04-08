# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:56:25 2021

@author: HITESH
"""


# =============================================================================
# Template Matching
# =============================================================================

dir='D:/Python/Deep Learning & Computer Vision, Open CV/Computer-Vision-with-Python/DATA/'

'''
Template Matching is the simplest form of object detection 
It scans a larger image for a provided template by sliding the template target image across the larger image


The main option that can be adjusted is the comparison method used as the target template is slid across the larger image
the methods are same sort of correlation based metric
'''


import cv2
import numpy as np
import matplotlib.pyplot as plt

full = cv2.imread(dir+'sammy.jpg')
full = cv2.cvtColor(full, cv2.COLOR_BGR2RGB)
#plt.imshow(full)

face = cv2.imread(dir+'sammy_face.jpg')
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
#plt.imshow(face)

# =============================================================================
# mystring = 'sum'
# eval(mystring) #can evaluate a string as if it is a funtion
# myFunc = eval(mystring)
# print(myFunc([1,2,3]))
# =============================================================================


methods = ['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']

for m in methods:
    
    # CREATE A COPY
    full_copy = full.copy()
    method = eval(m)
    
    # TEMPLATE MATCHING
    res = cv2.matchTemplate(full_copy, face, method)
    
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
    
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    
    height,width,channel = face.shape
    
    bottom_right = (top_left[0]+width, top_left[1]+height)
    cv2.rectangle(full_copy, top_left, bottom_right, (255,0,0),10)
    
    # PLOT AND SHOW IMAGES
    
    plt.subplot(121)
    plt.imshow(res)
    plt.title('HEAT MAP OF TEMPLATE MATCHING')
    
    plt.subplot(122)
    plt.imshow(full_copy)
    plt.title('DETECTION OF TEMPLATE')
    # TITLE WITH METHOD USED
    plt.suptitle(m)
    
    plt.show()
    
    print('\n')
    print('\n')
    