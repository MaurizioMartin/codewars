# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:22:49 2019

@author: macl3

URL: https://www.codewars.com/kata/deodorant-evaporator/train/python
"""


def evaporator(content, evap_per_day, threshold):
    days=0
    limit = content*(threshold/100)
    while content >= (limit):
        content -= (content*(evap_per_day/100))
        days += 1
    return days

    
def evaporator1(content,evap_per_day,threshold):
    return [days for days in range()]

def hola(content,evap_per_day,threshold):
    iterable = content*threshold/100
    content = (content*(evap_per_day/100))
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break
evaporator(10, 10, 10)