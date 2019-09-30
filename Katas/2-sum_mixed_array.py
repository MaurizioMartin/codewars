# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 09:31:12 2019

@author: macl3

URL: https://www.codewars.com/kata/sum-mixed-array/train/python
"""
lista = [1,4,"3",1,"4",5,"5"]

def sum_mix(arr):
    for idx, e in enumerate(arr):
        if type(e) == str:
            arr[idx] = int(e)
    suma = sum(arr)
    return suma

#mejor respuesta encontrada
def sum_mix2(arr):
    return sum(map(int, arr))

def sum_mix3(arr):
    return sum(int(n) for n in arr)

print(sum_mix(lista))
print(sum_mix2(lista))
print(sum_mix3(lista))
