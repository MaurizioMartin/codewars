# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 09:47:18 2019

@author: macl3

URL: https://www.codewars.com/kata/buddy-pairs/train/python
"""

def proper(n,m):
    nproper =[]
    mproper =[]
    [nproper.append(num) for num in range(1,n) if n%num == 0]
    [mproper.append(mum) for mum in range(1,m) if m%mum == 0]
    return [sum(nproper),sum(mproper)]

def buddy(start, limit):
    return proper(start,limit)
    for idx in range(start,limit):
        pass
        
        '''
        if start+1 == proper(start,limit)[1] and limit+1 == proper(start,limit)[0]:
            return [start,limit] 
        else:
            return "Nothing"
        '''
    
print(buddy(48,75))

