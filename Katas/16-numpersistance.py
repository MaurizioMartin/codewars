# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:32:02 2019

@author: macl3

URL: https://www.codewars.com/kata/persistent-bugger/train/python
"""
import numpy

def prod(n):
    return numpy.prod([int(i) for i in str(n)]) 

def persistence(n): 
    cont=0
    while len(str(n)) != 1:
        n = prod(n)
        cont+=1
    return cont

print(persistence(39)) # 3
print(persistence(4)) # 0
#persistence(25) # 2
print(persistence(999)) # 4
