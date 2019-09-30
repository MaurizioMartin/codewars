# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 09:46:16 2019

@author: macl3

URL: https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
"""

def count_sheep(n):
    counter=""
    for i in range(n):
        counter = counter+ str(i+1) + " sheep..."
    return counter
        
print(count_sheep(3))
