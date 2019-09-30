# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:32:28 2019

@author: macl3

URL: https://www.codewars.com/kata/ackermann-function/train/python
"""

def Ackermann(m,n):
    if m < 0 or n < 0:
        return None
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return Ackermann(m-1,1)
    elif m > 0 and n > 0:
        return Ackermann(m-1,Ackermann(m,n-1))
    
    
print(Ackermann(1,1)) #3
print(Ackermann(4,0)) #13