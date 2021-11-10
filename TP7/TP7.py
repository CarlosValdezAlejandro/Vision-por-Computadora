#!/usr/bin/env python
# coding: utf-8

# Trabajo Práctico N°7

# In[14]:


#!/usr/bin/env python
# coding: utf-8


import numpy as np
import cv2
red = (0,0,255)

drawing=False
xybutton_down = -1, -1
points = []
def affine(image, src_coord, dst_coord):
    (h, w) = image.shape[:2]
    M = cv2.getAffineTransform(src_coord, dst_coord)
    affine = cv2.warpAffine(image, M, (w, h)) #borderValue = BORDER_TRANSPARENT
    
    return affine


def mouse_points(event, x, y, flags, param):
    global img_point, img_point
    if event == cv2.EVENT_LBUTTONDOWN:
            points.append([x, y])
            cv2.circle(img_point, (x, y), 3, red, -1)
    
            

def selected_points(image):
    cv2.namedWindow('Selección de tres (3) puntos')
    cv2.setMouseCallback('Selección de tres (3) puntos', mouse_points)
    
    while(1):
        cv2.imshow('Selección de tres (3) puntos', image)
        k = cv2.waitKey(1)
        if len(points) == 3:
            break
    cv2.destroyAllWindows()
    
    return np.array(points, dtype = np.float32)
    

        

def read_img():
    global img, img2, img_copy, img2_copy, h,w , h_2, w_2
    img = cv2.imread('lenna.png', cv2.IMREAD_COLOR)
    h,w = img.shape[:2]
    img2 = cv2.imread('bandera.png', cv2.IMREAD_COLOR)
    img2 = cv2.resize(img2, img.shape[1::-1])
    h_2,w_2 = img.shape[:2]
    
    img_copy = img.copy()
    img2_copy = img2.copy()
    
    
    
read_img()
img_new = np.zeros((h,w,3), np.uint8)



cv2.namedWindow('image')

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('r'):
        read_img()
    elif k == ord('a'):
        img_point = img_copy
        src_coord = np.float32([[0,0],[w_2,0],[0,h_2]])
        dst_coord = selected_points(img_point)
        
        img_affined = affine(img2_copy, src_coord, dst_coord)
        cv2.imshow('resultado', img_affined)
        
        img_affined_gray = cv2.cvtColor(img_affined, cv2.COLOR_BGR2GRAY)
        
        
        #Lo hago con gris porque sino da error
        masked = cv2.bitwise_and(img, img, mask=img_affined_gray)
        cv2.imshow('Masked', masked)
        
        inv_masked = cv2.bitwise_xor( masked,img)
        cv2.imshow('Masked_n', inv_masked)
        
        
        img_n = cv2.add(inv_masked, img_affined)
        cv2.imshow('add', img_n)
        
        
    elif k == ord('q'):
        break

cv2.destroyAllWindows()

