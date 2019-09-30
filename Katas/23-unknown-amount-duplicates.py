# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:27:53 2019

@author: macl3

URL: https://www.codewars.com/kata/unknown-amount-of-duplicates-one-missing-number/train/python
"""
def list_duplicates(arr):
    dupli = set()
    add_dupli = dupli.add
    dupli_twice = [x for x in arr if x in dupli or add_dupli(x)]
    dupli_twice.sort()
    return dupli_twice

def find_dups_miss(arr):
    maxim=max(arr)
    minim=min(arr)
    arruniq=set(arr)
    missing = [i for i in range(minim,maxim) if i not in arruniq]
    return [missing[-1],list_duplicates(arr)]


'''
    def find_dups_miss(arr):
    maxim=max(arr)
    minim=min(arr)
    arruniq=set(arr)
    missing = [i for i in range(minim,maxim) if i not in arruniq]
    #uniq = [x for x in arruniq if arr.count(x) > 1]
    #uniq = [x for n, x in enumerate(arr) if x in arr[:n]]
    #uniq.sort()
    return [missing[-1],list_duplicates(arr)]
'''



arr1 = [10,9,8,9,6,1,2,4,3,2,5,5,3]
print(find_dups_miss(arr1)) # [7, [2, 3, 5, 9]]

arr2 = [20,19,6,9,7,17,16,17,12,5,6,8,9,10,14,13,11,14,15,19]
print(find_dups_miss(arr2)) #[18, [6, 9, 14, 17, 19]])

arr3 = [24,25,34,40,38,26,33,29,50,31,33,56,35,36,53,49,57,27,37,40,48,44,32,35,45,52,43,47,26,51,55,28,41,42,46,51,25,30,44,54]
print(find_dups_miss(arr3)) #[39, [25, 26, 33, 35, 40, 44, 51]])
