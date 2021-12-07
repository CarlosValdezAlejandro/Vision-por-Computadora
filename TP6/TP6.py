#!/usr/bin/env python
# coding: utf-8

# Trabajo Práctico N°6

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# Trabajo Práctico N°6


import numpy as np
import cv2

blue = (255,0,0); green = (0,255,0); red = (0,0,255)
drawing=False
xybutton_down = -1, -1

def translate(image, angle, x_t, y_t, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    angle = np.radians(angle)
    M = np.float32([[scale*np.cos(angle), scale*np.sin(angle), x_t],
                    [scale*-np.sin(angle), scale*np.cos(angle), y_t]])

    
    translate = cv2.warpAffine(image, M, (w, h))
    return translate


def input_values():
    global angle, x, y, scale
    angle = float(input('ingrese angulo de traslación: '))
    x =  int(input('ingrese traslación en x: '))
    y =  int(input('ingrese traslación en y: '))
    scale= float(input('ingrese valor de escala: '))
    
    
    
def dibuja(event, x, y, flags, param):
    global drawing, mode, xf, yf, xi, yi
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        xi, yi = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            img[:] = img_copy[:]
            cv2.rectangle(img, (xi, yi), (x,y), blue, 2)
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
    elif k == ord('g'):
        img_copy = img_copy[yi:yf, xi:xf]
        img_translate = translate(img_copy, angle, x, y, None , scale)
        cv2.imwrite('lenna_croped&translated.png', img_translate)
        cv2.imshow('imagen guardada', img_translate)
        
        
    elif k == ord('q'):
        break

cv2.destroyAllWindows()


# In[ ]:




