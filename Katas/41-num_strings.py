# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:34:43 2019

@author: macl3

URL: https://www.codewars.com/kata/numericals-of-a-string/train/python
"""

def numericals(s):
    string = ""
    dictio = {}
    for e in s:
        if e in dictio:
            dictio[e] = dictio[e]+1
            string += str(dictio[e])
        else:
            dictio[e] = 1
            string += str(dictio[e])
    return string

# refactorized
    
def numericals2(s):
    string = ""
    dictio = {}
    for e in s:
        dictio[e] = dictio.get(e,0) + 1 
        string += str(dictio[e])
    return string

print(numericals("Hello, World!")) # "1112111121311")
print(numericals("Hello, World! It's me, JomoPipi!")) # "11121111213112111131224132411122")
print(numericals("hello hello")) # "11121122342")
print(numericals("Hello")) # "11121")
print(numericals("aaaaaaaaaaaa")) #"123456789101112")
