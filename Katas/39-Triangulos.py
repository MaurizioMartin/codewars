# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:33:48 2019

@author: macl3

Prueba Deliveroo

Calcula 100 triángulos rectángulos diferentes y muestra sus dos catetos y su hipotenusa
"""

import random
from math import sqrt

x = 100
def calcHipo(a,b):
    return sqrt((a*a)+(b*b))

def calcHipo2(a,b):
    return ((a**2)+(b**2))**0.5

for i in range(x):
    catetoa = random.randint(1,x)
    catetob = random.randint(1,x)
    print("{} - Cateto A = {}, Cateto B = {}, Hipotenusa = {}".format(i,catetoa,catetob,calcHipo(catetoa,catetob)))
    print("{} - Cateto A = {}, Cateto B = {}, Hipotenusa = {}".format(i,catetoa,catetob,calcHipo2(catetoa,catetob)))

# Otra manera:

for i in range(1,101):
    print("Cateto A: {}, Cateto B: {}, Hipotenusa: {}".format(i,i,calcHipo(i,i)))
    
# Otra manera:
    
for i in range(1,101):
    print("Cateto A: {}, Cateto B: {}, Hipotenusa: {}".format(i,i,((i**2)+(i**2))**0.5))
   
    
# Otra manera:
    
for b in range(1,101):
  for c in range(b,101):
    a=(b**2+c**2)**.5
    if a == int(a):
      print(b,c,int(a))
      
      
#Solución Deliveroo
      
x = 1
for i in range(100):
    y = 2*(x**2)
    print(x,x,y)
    x=x+1

    