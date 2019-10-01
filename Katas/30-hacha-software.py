# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:47:44 2019

@author: macl3

URL: https://www.codewars.com/kata/computer-problem-series-number-3-hacha-software-split/train/python
"""
import re

def split(string, split_len):
    regex = r'(.{%s})' % split_len
    return [x for x in re.split(regex, string) if x]

def hacha(file, size): 
    lista = []
    if file["data"] == "":
        return []
    else:
        data = split(file["data"],size)
        long = len(str(len(data)))
        cont = 1
        for e in data:
            lista.append({"name":file["name"]+"."+str(cont).zfill(long), "data": e})
            cont+=1
        return lista

file = {"name": "ex.py", "data": "abcdefghijkl"}
size = 6
file2 = {"name": "ex.py", "data": "12345678"}
size2 = 3
file3 = {"name": "ex.py", "data": "1234567890"}
size3 = 1
print(hacha(file,size))
print(hacha(file2,size2))
print(hacha(file3,size3))