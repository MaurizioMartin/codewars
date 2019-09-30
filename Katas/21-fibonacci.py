# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:25:35 2019

@author: macl3

URL: https://www.codewars.com/kata/fibonacci-tribonacci-and-friends/train/python
"""

def Xbonacci(signature,n):
    num = len(signature)
    fibonacci=signature
    fibonacci.append(sum(signature))
    if n > num:
        for x in range(len(fibonacci),n):       
            fibonacci.append(sum(fibonacci[-num:]))
        return fibonacci
    else:
        return signature[:n]
    
    
#print(fibonacci) 
print(Xbonacci([0,1],10)) #[0,1,1,2,3,5,8,13,21,34])
print(Xbonacci([1,1],10)) #[1,1,2,3,5,8,13,21,34,55])
print(Xbonacci([0,0,0,0,1],10)) #[0,0,0,0,1,1,2,4,8,16])
print(Xbonacci([1,0,0,0,0,0,1],10)) #[1,0,0,0,0,0,1,2,3,6])
print(Xbonacci([1,0,0,0,0,0,0,0,0,0],20)) #[1,0,0,0,0,0,0,0,0,0,1,1,2,4,8,16,32,64,128,256])
print(Xbonacci([8, 4, 16, 0, 9, 5, 20, 0, 14, 12],1))

