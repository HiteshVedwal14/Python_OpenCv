# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:57:14 2021

@author: HITESH
"""

'''
HARRIS CORNER DETECTION:
    The basic intuition is that corners can be detected by looking for significant change in all directions

SHI-TOMASI CORNER DETECTION 
'''

dir='D:/Python/Deep Learning & Computer Vision, Open CV/Computer-Vision-with-Python/DATA/'

import cv2
import numpy as np
import matplotlib.pyplot as plt

flat_chess = cv2.imread(dir+'')

