# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:08:33 2021

@author: HITESH
"""



# =============================================================================
# DRAWING ON A LIVE CAMERA
# =============================================================================



import cv2

'''
cap = cv2.VideoCapture(0)


width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# Drawing a rectangle in a live video

x = width //2
y = height //2

# Width and Height of the rectangle 
w = width //4
h = height //4



while True:
    
    ret,frame = cap.read()
    
    cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,0,255),thickness=4)
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''


# INTERACT WITH VIDEO

## CALLBACK FUNCION RECTANGLE

def draw_rectangle(event, x, y, flags, param):
    
    global pt1, pt2, topLeftClicked, botLeftClicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        # RESET THE RECTANGLE (IT CHECKS IF THE RECTANGLE IS THERE)
        if topLeftClicked == True and botLeftClicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeftClicked = False
            botLeftClicked = False
        
        if topLeftClicked == False:
            pt1 = (x,y)
            topLeftClicked = True
            
        elif botLeftClicked == False:
            pt2 = (x,y)
            botLeftClicked = True

## GLOBAL VARIABLES

pt1 = (0,0)
pt2 = (0,0)
topLeftClicked = False
botLeftClicked = False

## CONNECT TO THE CALLBACK

cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)

while True:
    
    ret,frame = cap.read()
    
    # DRAWING ON THE FRAME BASED OFF THE GLOBAL VARIABLES
    
    if topLeftClicked:
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)
    
    if topLeftClicked and botLeftClicked:
        cv2.rectangle(frame, pt1, pt2, (0,0,255), 3)
        
    
    cv2.imshow('Test', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

