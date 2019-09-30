# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:26:16 2019

@author: macl3

URL: https://www.codewars.com/kata/simple-fun-number-312-maximum-product/train/python
"""
from functools import reduce
import numpy as np

def maximum_product_solve(arr):
    result = 1
    for x in arr: 
         result = result * x  
    return result  

def maximum_product(arr):
    reslist=[]
    for elem in range(len(arr)):  
        reslist.append(maximum_product_solve(arr[:elem])*maximum_product_solve(arr[elem+1:]))
    result = reslist.index(max(reslist))
    return arr[result]
        
    
def maximum_product2(arr):
    totals = []
    arr=sorted(arr)
    for i in range(len(arr)):
        totals.append(reduce(lambda a,b: a*b, arr[:i]+arr[i+1:]))
    return arr.pop(totals.index(max(totals)))

def maximum_product3(arr):
    to_r = arr[0]
    to_rv = np.prod(arr[1:])
    for i in range(len(arr)):
        prod = np.prod((arr[:i]+arr[i+1:]))
        if prod >= to_rv:
            if prod==to_rv:
                to_r = min(arr[i],to_r)
            else:
                to_r = arr[i]
                to_rv =  np.prod((arr[:i]+arr[i+1:]))
    return to_r

print(maximum_product([0, -1, -2, -3]))
print(maximum_product3([0, -1, -2, -3]))

#print(maximum_product([1, 2, 3]))
#print(maximum_product([-1, -2, -3, -4]))