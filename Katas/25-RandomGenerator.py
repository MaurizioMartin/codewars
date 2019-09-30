# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:30:51 2019

@author: macl3

URL: https://www.codewars.com/kata/write-your-own-pseudorandom-number-generator/train/python
"""
import time

class Random():
    def __init__(self, seed):
        self.seed = seed
    def random(self):
        ranumb = round(time.time())
        ranumb2 = ranumb / self.seed
        return round(self.seed * ranumb - ranumb2)
    def randint(self, start, end):
        ranumb = round(time.time())
        return round(start + end / ranumb + 23)
    
random = Random(10)
print(random.random())
print(random.randint(20,60))
