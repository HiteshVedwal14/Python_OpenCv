# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:58:29 2021

@author: HITESH
"""


# =============================================================================
# Using Existing Video Files
# =============================================================================


import cv2
import time

dir='D:/Python/'


cap = cv2.VideoCapture(dir+'mysupervideo.mp4')

if cap.isOpened() == False:
    print('Error file not found or wrong codec used')
    
while cap.isOpened():
    
    ret,frame = cap.read()
    
    if ret == True:
        
        # WRITER 20fps
        time.sleep(1/25)            # To be able to view the video for human
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    else:
        break
cap.release()
cv2.destroyAllWindows()