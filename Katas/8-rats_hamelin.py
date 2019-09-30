# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:35:44 2019

@author: macl3

URL: https://www.codewars.com/kata/the-deaf-rats-of-hamelin/train/python
"""
import re

def count_deaf_rats(town):
    p=town.split("P")
    r = [''.join(rats) for rats in re.findall('(~O)|(O~)', p[0])]
    l = [''.join(rats) for rats in re.findall('(~O)|(O~)', p[1])]
    return r.count('O~') + l.count('~O')


                
print(count_deaf_rats("~O~O~O~OPO~O~O~ O~O~O~O~O~O~O~O~O~ O~O~O~O~O~~OO~O~O~O~O~O~O~~OO~ O~O~O~O~O~ O~ O~O~O~O~ O~O~O~"))
print(count_deaf_rats("~O~O~O~O P"))
print(count_deaf_rats("~O~O~O~OP~O~OO~"))
print(count_deaf_rats("P O~ O~ ~O O~"))