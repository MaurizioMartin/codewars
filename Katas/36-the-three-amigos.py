# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 09:34:39 2019

@author: macl3

URL: https://www.codewars.com/kata/the-three-amigos/train/python
"""

def parity(n):
    if n%2 == 0:
        return 0
    else:
        return 1
    
def checkList(n,n2,n3):
    if parity(n) == 0:
        if parity(n2) == 0:
            if parity(n3) == 0:
                lista = [n,n2,n3]
                dif = max(lista) - min(lista)
                return lista,dif
    else:
        if parity(n2) == 1:
            if parity(n3) == 1:
                lista = [n,n2,n3]
                dif = max(lista) - min(lista)
                return lista,dif

def three_amigos(numbers):
    lista = []
    for v in range(len(numbers)):
        if v < len(numbers)-2:
            trienio = checkList(numbers[v],numbers[v+1],numbers[v+2])
            if trienio != None:
                lista.append(trienio)
    lista.sort(key = lambda x: (x[1]))
    if len(lista) > 0:
        return lista[0][0]
    else:
        return lista
    
    
# Mejor solución         
def three_amigosFel(numbers):
    trip = sorted([numbers[i:i+3] for i in range(len(numbers)-2) if numbers[i]%2==numbers[i+1]%2==numbers[i+2]%2], key=lambda x: max(x)-min(x))
    return trip[0] if trip else []



print(three_amigos([1, 2, 34, 2, 1, 5, 3, 5, 7, 234, 2, 1])) # [5,3,5])
print(three_amigos([2, 4, 6, 8, 10, 2, 2, 2, 1, 1, 1, 5, 3])) # [2,2,2])
print(three_amigos([2, 4, 5, 3, 6, 3, 1, 56, 7, 6, 3, 12])) # [])