# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:27:05 2019

@author: macl3

URL: https://www.codewars.com/kata/schrodingers-boolean/train/python
"""

class Omnibool:
    def __init__(self):
        pass
    def __eq__(self,other):
        return True

omnibool = Omnibool()

'''
test.describe('Basic Tests')
test.expect(omnibool == True)
test.expect(omnibool == False)
print('<COMPLETEDIN::>')
'''