#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# Trabajo Práctico N°5

# In[1]:


#! /usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import cv2

blue = (255,0,0); green = (0,255,0); red = (0,0,255)
drawing=False
xybutton_down = -1, -1

def similarity(image, angle, x_t, y_t, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    angle = np.radians(angle)
    M = np.float32([[scale*np.cos(angle), scale*np.sin(angle), x_t],
                    [scale*-np.sin(angle), scale*np.cos(angle), y_t]])

    
    translate = cv2.warpAffine(image, M, (w, h))
    return translate


def input_values():
    global angle, x, y, scale
    angle = int(input('ingrese angulo de traslación: '))
    x =  int(input('ingrese traslación en x: '))
    y =  int(input('ingrese traslación en y: '))
    scale=int(input('ingrese valor de escala: '))
    
    
    
def dibuja(event, x, y, flags, param):
    global xybutton_down, drawing, mode, xf, yf, xi, yi
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        xi, yi = x, y
        xybutton_down = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            img = img_copy.copy()
            cv2.rectangle(img, xybutton_down, (x,y), blue, 2)
            xf, yf = x, y
        
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.imshow('imagen seleccionada', img_copy[yi:yf, xi:xf])
        

def read_img():
    global img, img_copy
    img = cv2.imread('lenna.png', cv2.IMREAD_COLOR)
    img_copy = img.copy()
    
    
read_img()
cv2.namedWindow('image')
input_values()
cv2.setMouseCallback('image', dibuja)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('r'):
        read_img()
    elif k == ord('s'):
        img_copy = img_copy[yi:yf, xi:xf]
        img_translate = similarity(img_copy, angle, x, y, None , scale)
        cv2.imwrite('lenna_crop_trans_sca.png', img_similarity)
        cv2.imshow('imagen guardada', img_similarity)
        
        
    elif k == ord('q'):
        break

cv2.destroyAllWindows()

