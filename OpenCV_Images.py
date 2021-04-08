# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 19:27:15 2021

@author: HITESH
"""


# Opening Image files Notebook
import matplotlib.pyplot as plt
import numpy as np
import cv2

#img = cv2.imread('00-puppy.jpg')
#type(img)


# MATPLOTLIB -> RGB: RED, GREEN, BLUE
# OPEN CV -> BGR

#plt.imshow(img)

#fixed_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#plt.imshow(fixed_img)

'''img_gray = cv2.imread('00-puppy.jpg', cv2.IMREAD_GRAYSCALE)
img_gray.shape
img_gray.max
img_gray.min
plt.imshow(img_gray, cmap='gray')
'''

#plt.imshow(fixed_img)

#new_img = cv2.resize(fixed_img,(1000,400))
#plt.imshow(new_img)


'''w_ratio = 0.5
h_ratio = 0.5
new_image = cv2.resize(fixed_img,(0,0),fixed_img,w_ratio,h_ratio)
plt.imshow(new_image)
new_image.shape
'''

#new_im = cv2.flip(fixed_img,0)
#plt.imshow(new_im)
#type(fixed_img)

#cv2.imwrite('totally_new.jpg',fixed_img)

'''fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.imshow(fixed_img)'''

'''
blank_img = np.zeros(shape=(512,512,3),dtype=np.int16)
blank_img.shape
plt.imshow(blank_img)

### Below is the rectangle
cv2.rectangle(blank_img,pt1=(384,10),pt2=(500,150),color=(0,255,0),thickness=10)
plt.imshow(blank_img)

### Below is the square
cv2.rectangle(blank_img,pt1=(200,200),pt2=(300,300),color=(0,0,255),thickness=10)
plt.imshow(blank_img)

### Below is the circle
cv2.circle(img=blank_img,center=(100,100),radius=50,color=(255,0,0),thickness=10)
plt.imshow(blank_img)

### Circle filled with color
cv2.circle(img=blank_img,center=(400,400),radius=50,color=(255,0,0),thickness=-1)
plt.imshow(blank_img)

### Line 
cv2.line(img=blank_img,pt1=(0,0),pt2=(512,512),color=(102,255,255), thickness = 5)
plt.imshow(blank_img)


### Text written
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img, text='Hello',org=(10,500),fontFace=font,fontScale=4,color=(255,255,255),
            thickness=3,lineType=cv2.LINE_AA)
plt.imshow(blank_img)
'''



'''
blank_img = np.zeros(shape=(512,512,3),dtype=np.int32)
plt.imshow(blank_img)
vertices = np.array([[100,300], [200,200], [400,300], [200,400]],dtype=np.int32)
vertices.shape
pts = vertices.reshape((-1,1,2))
cv2.polylines(blank_img,[pts],isClosed=True,color=(255,0,0),thickness=5)
plt.imshow(blank_img)
'''

##########################################################################################################################
'''
# Connecting callback funtions
# Draw with mouse

###############
## FUNCTIONS ##
###############

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),-1)
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)

###############################
## SHOWING IMAGE WITH OPENCV ##
###############################

img = np.zeros(shape=(512,512,3))

while True:
    cv2.imshow('my_drawing',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows() 


'''

#######################################################################################################################
'''
# Connecting callback funtions
# Draw with mouse

###############
## FUNCTIONS ##
###############

# True while mouse button down, False while mouse button 
drawing = False
ix,iy=-1,-1

def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_rectangle)

###############################
## SHOWING IMAGE WITH OPENCV ##
###############################

img = np.zeros(shape=(512,512,3))

while True:
    cv2.imshow('my_drawing',img) 
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
'''


img = cv2.imread('D:/Python/Deep Learning & Computer Vision, Open CV/Computer-Vision-with-Python/DATA/dog_backpack.jpg')
img2 = img.copy()

cv2.rectangle(img2,pt1=(210,380),pt2=(600,720),color=(0,0,255),thickness=10)
plt.imshow(img2)

