#!/usr/bin/env python
# coding: utf-8

# Trabajo Práctico N°4

# In[4]:


#! /usr/bin/env python
# -*- coding: utf-8 -*-


import cv2
import numpy as np

blue = (255,0,0); green = (0,255,0); red = (0,0,255)
drawing=False

xybutton_down = -1, -1

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
cv2.setMouseCallback('image', dibuja)


while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('r'):
        read_img()
    elif k == ord('g'):
        img_copy = img_copy[yi:yf, xi:xf]
        cv2.imwrite('lenna_croped.png', img_copy)
        cv2.imshow('imagen guardada', img_copy)
        
    elif k == ord('q'):
        break

cv2.destroyAllWindows()

