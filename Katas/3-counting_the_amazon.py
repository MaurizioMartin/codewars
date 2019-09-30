# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 09:25:52 2019

@author: macl3

URL: https://www.codewars.com/kata/counting-in-the-amazon/train/python


1 = anane 
2 = adak 
3 = adak anane 
4 = adak adak 
5 = adak adak anane 
6 = adak adak adak
7 = adak adak adak anane
8 = adak adak adak adak 
"""

def count_arara(n):
    ad = "adak"
    ade = "adak "
    an =  "anane"
    if n % 2 == 0:
        result = int((n/2)-1)*ade + ad
    else:
        if n == 1:
            result = an
        else:
            result = int((n-1)/2)*ade + an
    return result       



#respuesta bego
def count_arara3(n):
  count = []
  count += ["adak"] * int((n/2))
  if n % 2 != 0:
    count += ["anane"]
  return " ".join(count)

#mejor respuesta encontrada
def count_arara2(n):
    return " ".join(['adak']*(n//2) + ['anane']*(n%2))

print(count_arara(5))
print(count_arara2(5))
print(count_arara3(5))
