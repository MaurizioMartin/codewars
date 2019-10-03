# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:29:14 2019

@author: macl3

URL: https://www.codewars.com/kata/perimeter-of-squares-in-a-rectangle/train/python
"""

def perimeter(n):
    anterior = 1
    posterior = 1
    fibonacci=[anterior,posterior]
    
    for x in range(1,n):
        fib = anterior + posterior
        anterior = posterior
        posterior = fib
        fibonacci.append(fib)
        
    return(4*sum(fibonacci))
    
print(perimeter(5)) # 80)
print(perimeter(7)) # 216)
print(perimeter(20)) # 114624)
print(perimeter(30)) # 14098308)
print(perimeter(100)) # 6002082144827584333104)