#!/usr/bin/env python
# coding: utf-8

# Trabajo Práctico N° 8

# In[18]:


#!/usr/bin/env python
# coding: utf-8


import numpy as np
import cv2


red = (0,0,255)

drawing=False
xybutton_down = -1, -1
points = []

def perspective(image, src_coord, dst_coord):
    (h, w) = image.shape[:2]
    M = cv2.getPerspectiveTransform(src_coord, dst_coord)
    rectified = cv2.warpPerspective(img, M, (w, h))
    
    return rectified

def mouse_points(event, x, y, flags, param):
    global img_point, img_point
    if event == cv2.EVENT_LBUTTONDOWN:
            points.append([x, y])
            cv2.circle(img_point, (x, y), 3, red, -1)
    
            

def selected_points(image):
    cv2.namedWindow('Selección de tres (4) puntos')
    cv2.setMouseCallback('Selección de tres (4) puntos', mouse_points)
    
    while(1):
        cv2.imshow('Selección de tres (4) puntos', image)
        k = cv2.waitKey(1)
        if len(points) == 4:
            break
    cv2.destroyAllWindows()
    
    return np.array(points, dtype = np.float32)
    

        

def read_img():
    global img, img_copy, h,w, new_h, new_w
    img = cv2.imread('Raid.jpg', cv2.IMREAD_COLOR)
    h,w = img.shape[:2]
    if h > 1080:
        scale_h = 768/h
        #scale_w = 1920/w
        new_h, new_w = int(scale_h*h), int(scale_h*w)
        img = cv2.resize(img, (new_h, new_w))
        h,w = img.shape[:2]
    elif w>1920:
        scale_w = 1366/w
        new_h, new_w = int(scale_w*h), int(scale_w*w)
        img = cv2.resize(img, (new_h, new_w))
        h,w = img.shape[:2]
        
    img_copy = img.copy()
    
    
    
read_img()

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    
    if k == ord('h'):
        cv2.destroyAllWindows()
        img_point = img_copy
        dst_coord = np.float32([[0,0],[w,0],[w,h],[0,h]])
        src_coord = selected_points(img_point)
        img_copy = perspective(img_copy, src_coord, dst_coord)
        cv2.imshow('Image Rectified',img_copy)
        
        cv2.imwrite('rectified.png', img_copy)
              
    elif k == ord('q'):
        break

cv2.destroyAllWindows()

