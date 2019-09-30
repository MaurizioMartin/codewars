# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 09:30:42 2019

@author: macl3

URL: https://www.codewars.com/kata/sorting-by-bits/train/python
"""
#mia
def sort_by_bit(arr): 
    order_list = []
    for e in arr:
        ebin = bin(e).count("1")
        order_list.append([e,ebin])
    order_list.sort(key=lambda elem: (elem[1], elem[0]))
    final_list = [e[0] for e in order_list]
    return final_list

#mejor respuesta
def sort_by_bit2(arr): 
    return sorted(arr, key=lambda x: (bin(x).count("1"), x))

#mia 2.0
def sort_by_bit3(arr):
    order_list = [[e,bin(e).count("1")] for e in arr]
    order_list.sort(key=lambda elem: (elem[1], elem[0]))
    return [e[0] for e in order_list]
    
#mia 3.0
def sort_by_bit4(arr):
    order_list = [[e,bin(e).count("1")] for e in arr]
    return [e[0] for e in sorted(order_list, key=lambda elem: (elem[1], elem[0]))]

arr = [3, 8, 3, 6, 5, 7, 9, 1]

print(sort_by_bit4(arr))