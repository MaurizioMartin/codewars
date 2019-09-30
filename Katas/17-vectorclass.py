# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:29:42 2019

@author: macl3

URL: https://www.codewars.com/kata/vector-class/train/python

"""
import math
import re

class Vector:
    def __init__(self,lista):
        self.lista = lista
        self.len = len(lista)
        
    def add(self, lista):
        if self.len == lista.len:
            return Vector([x+y for x,y in zip(self.lista, lista.lista)])
    
    def subtract(self, lista):
        if self.len == lista.len:
            return Vector([x-y for x,y in zip(self.lista, lista.lista)])
    
    def dot(self, lista):
        if self.len == lista.len:
            return sum([x*y for x,y in zip(self.lista, lista.lista)])
    
    def norm(self):
        potencias = [x**2 for x in self.lista]
        return math.sqrt(sum(potencias))
        
    def equals(self,lista):
        if self.lista == lista.lista:
            return True
        else:
            return False
            
    def __str__(self):
        return re.sub(" ","",str(tuple(self.lista)))
 
a = Vector([1, 2])
b = Vector([3, 4])
print(a.toString)
print(a.add(b).toString)
print(a.subtract(b))
print(a.norm())
print(a.dot(b))
