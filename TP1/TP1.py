#!/usr/bin/env python
# coding: utf-8

# Practico numero 1

# In[ ]:


import random


def adivinar(intentos):
    
    #numero aleatorio 0-100
    num = random.randint(0, 100)
    i=0
    resultado = False
    
    while(i <= intentos):
        while True:
            try:
                num_usuario = int(input('Ingrese numero para adivinar: '))
                break
            except:
                print("Entrada incorrecta")
        
        if(num_usuario == num):
            resultado = True
            break
        i+=1
    return resultado, i
        
          
    

while True:
        try:
            n_intentos = int(input('Ingrese cantidad de intentos: '))
            break
        except:
            print("Entrada incorrecta")

result, i = adivinar(n_intentos)

if(result):
    print("Numero adivinado correctamente")
    print("usted adivino el numero en el intento nro: ", i)
else:
    print("Maxima cantidad de intentos")
    


