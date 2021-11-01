#!/usr/bin/env python
# coding: utf-8

# Trabajo Práctico N°3

# In[4]:


#!/usr/bin/python
# -*- coding: utf-8 -*-


import cv2 as cv

#define un objeto de captura de video
cap = cv.VideoCapture('The_Seed.avi')

#especificamos formato
fourcc_XVID = cv.VideoWriter_fourcc('X', 'V', 'I', 'D') #.avi codificacion de video xvid
#obtengo fps con metodo de cv2. puedo reemplazar por cap.get(5)
fps = cap.get(cv.CAP_PROP_FPS)
#ancho y alto sin hardcodear con metodo cv2
framesize = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

#delay en milisegundos
delay = int(1000/fps)

#read devuelve una tupla, primer elemento booleano, segundo frame
success, frame = cap.read() #Success indica captura exitosa

if not success:
    print("no se pudo realizar captura")

out = cv.VideoWriter('video_xvid.avi', fourcc_XVID, fps, framesize, isColor=False)

while success:
    #convierte a escala de grises
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    out.write(gray)
    cv.imshow('Image gray', gray)
    #espera delay ms a que presione tecla Q
    if (cv.waitKey(delay) & 0xFF) == ord('q'):
        break
    #leemos otro cuadro sino apretamos Q
    success, frame = cap.read()
        
cap.release()
out.release()
cv.destroyAllWindows()

