#!/usr/bin/env python
# coding: utf-8

# Trabajo Práctico N°9

# In[12]:


#!/usr/bin/env python
# coding: utf-8


import numpy as np
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
rectified_flag = False
red = (0,0,255); blue = (255,0,0); green = (0,255,0)
drawing=False
xybutton_down = 0, 0
points = []
xf, yf, xi, yi = 0,0,0,0

name_image = 'fachada.jpg'
        
#f linea calibrar
def linea(event, x, y, flags, param):
    global xybutton_down, drawing, mode, xf, yf, xi, yi, img_rect
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        xi, yi = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            img_rect[:] = img_rect_copy[:]
            cv2.line(img_rect, (xi, yi), (x,y), blue, 3)
            xf, yf = x, y
                    
    elif event == cv2.EVENT_LBUTTONUP:
        img_rect_copy[:] = img_rect[:]
        drawing = False
        print("coordenadas" ,xi, xf, yi, yf)
        
#f linea y texto para medicion
def line_measure(event, x, y, flags, param):
    global drawing, mode, xf, yf, xi, yi, img_mea, distance
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        xi, yi = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:     
            img_mea[:] = img_mea_copy[:]
            cv2.line(img_mea, (xi, yi), (x,y), blue, 3)
            xf, yf = x, y
            px_distance = (np.sqrt((xf-xi)**2+(yf-yi)**2))
            distance = px_distance/c_calibration         
            loc_text = int((xi+xf)/2+10), int((yi+yf)/2-10)                
            img_rect = cv2.putText(img_mea, "{:.3f} cm".format(distance),loc_text, font, 1, green, 1)
            
        
    elif event == cv2.EVENT_LBUTTONUP:
        img_mea_copy[:] = img_mea[:]
        drawing = False
        print("La distancia del objeto medido es: ", distance)
        
        
#f rectificar imagen
def perspective(image, src_coord, dst_coord):
    (h, w) = image.shape[:2]
    M = cv2.getPerspectiveTransform(src_coord, dst_coord)
    rectified = cv2.warpPerspective(img, M, (w, h))
    
    flag = True
    
    return rectified, flag


def mouse_points(event, x, y, flags, param):
    global img_point, img_point
    if event == cv2.EVENT_LBUTTONDOWN:
            points.append([x, y])
            cv2.circle(img_point, (x, y), 3, red, -1)
            
    
            
#f para seleccion de puntos y obtener coordenadas para rectificar
def selected_points(image):
    cv2.namedWindow('Seleccion de cuatro puntos')
    cv2.setMouseCallback('Seleccion de cuatro puntos', mouse_points)
    
    while(1):
        cv2.imshow('Seleccion de cuatro puntos', image)
        k = cv2.waitKey(1)
        if len(points) == 4:
            break
    cv2.destroyAllWindows()
    
    return np.array(points, dtype = np.float32)
    

        
#funcion para achicar la img a monitor
def read_img(image):
    global img, img_copy, h,w, new_h, new_w
    img = cv2.imread(image, cv2.IMREAD_COLOR)
    h,w = img.shape[:2]
    img_copy = img.copy()
"""    
    if h > 1079:
        scale_h = 768/h
        #scale_w = 1920/w
        new_h, new_w = int(scale_h*h), int(scale_h*w)
        img = cv2.resize(img, (new_h, new_w))
        h,w = img.shape[:2]
    elif w>1919:
        scale_w = 1366/w
        new_h, new_w = int(scale_w*h), int(scale_w*w)
        img = cv2.resize(img, (new_h, new_w))
        h,w = img.shape[:2]
""" 
        

    

read_img(name_image)

while(1):
    
    #print("Seleccione 4 puntos para rectificar")
    k = cv2.waitKey(1) & 0xFF
    img_point = img_copy
    dst_coord = np.float32([[0,0],[w,0],[w,h],[0,h]])
    #src_coord = selected_points(img_point)
    src_coord = np.float32([[134 , 149],[1002 , 89],[997 , 729],[145 , 630]])
    print(src_coord)
    img_copy, rectified_flag = perspective(img_copy, src_coord, dst_coord)
    cv2.imshow('Image Rectified',img_copy)
    cv2.imwrite('rectified.png', img_copy)
    cv2.destroyAllWindows()
    
    if rectified_flag == 1:
        break
img_rect_copy = img_copy.copy()
img_rect =  img_rect_copy.copy()    

while(1):
    cv2.imshow('Presione c y seleccione dos puntos, luego e', img_rect)
    k = cv2.waitKey(1) & 0xFF
    
    if k == ord('c'):
        cv2.destroyAllWindows()
        cv2.namedWindow('Presione c y seleccione dos puntos, luego e')
        cv2.setMouseCallback('Presione c y seleccione dos puntos, luego e', linea)

    elif k == ord('e'):
        break

cv2.destroyAllWindows()

px_distance = (np.sqrt((xf-xi)**2+(yf-yi)**2))
print("Distancia en pixeles seleccionada: ", px_distance)
real_distance = float(input("Ingrese medida real de la distancia seleccionada: "))
c_calibration =  (px_distance/real_distance)
print("pixels/metro: ",c_calibration)

##
xf,xi,yi,yf=0,0,0,0

img_mea_copy = img_copy.copy()
img_mea = img_mea_copy.copy()

while(1):
    cv2.imshow('Presione m y seleccione dos puntos a medir', img_mea)
    k = cv2.waitKey(1) & 0xFF
    
    if k == ord('m'):
        cv2.destroyAllWindows()
        cv2.namedWindow('Presione m y seleccione dos puntos a medir')
        cv2.setMouseCallback('Presione m y seleccione dos puntos a medir', line_measure)
        
        
    elif k == ord('q'):
        break
        
    elif k == ord('r'):
        img_mea = img_mea_copy.copy()
        img_mea_copy = img_copy.copy()
    
    elif k == ord('g'):
        cv2.imwrite('Medidas.jpg',img_mea)
        break
##

cv2.destroyAllWindows()

#[[ 134.  149.]
# [1002.   89.]
# [ 997.  729.]
# [ 145.  630.]]


# In[ ]:




