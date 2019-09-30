# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.

URL: https://www.codewars.com/kata/piano-kata-part-1/train/python
"""

def black_or_white_key(key_press_count):
    p1 = ["white","black","white"]
    p2 = ["white","black","white","black","white","white","black","white","black","white","black","white"]

    total = p1+(p2*7)
    return total[(key_press_count%88)-1]

#best solution
def black_or_white_key2(key_press_count):
    return "black" if (key_press_count - 1) % 88 % 12 in [1, 4, 6, 9, 11] else "white"

print(black_or_white_key(1)) # "white")
print(black_or_white_key(5)) #"black")
print(black_or_white_key(12)) # "black")
print(black_or_white_key(42)) # "white")
print(black_or_white_key(88)) # "white")
print(black_or_white_key(89)) # "white")
print(black_or_white_key(92)) # "white")
print(black_or_white_key(100)) #"black")
print(black_or_white_key(111)) # "white")
print(black_or_white_key(200)) #"black")
print(black_or_white_key(2017)) # "white")