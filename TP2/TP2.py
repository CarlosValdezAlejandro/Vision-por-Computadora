#!/usr/bin/env python
# coding: utf-8

# Trabajo Practico N°2
# 

# In[5]:


#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2


img = cv2.imread ('hoja.png', 0) #leer en escala de grises los pixeles q no sean blanco y negro y estos van a estar entre 0 y 255


umbral = int(input('Valor del umbral entre 0-255: ')) #valor mas bajo, mas grises, mas alto mas negra la img
x , y= img.shape  #shape nos da la altura, ancho, y canal de color (no usado en nuestro caso) respectivamente

#for anidado para recorrer columnas y filas de la imagen 
for row in range(x):
    for col in range(y):
        if (img[row, col]  <= umbral): #limite de umbral para img
            img[row, col] = 0

#guardo archivo nuevo
cv2.imwrite('resultado.png', img)
#muestro archivo nuevo
cv2.imshow('Imagen Umbralizada', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

