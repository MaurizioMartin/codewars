# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:25:39 2019

@author: macl3

URL: https://www.codewars.com/kata/tests-results/train/python
"""

notasa = [10,9,9,10,9,10,9]
notasb = [5,6,4,8,9,8,9,10,10,10]

def test(r):
    dictnotas = {"h":0, "a":0, "l":0}
    returnlist = []
    average = round(sum(r)/len(r),3)
    for elem in r:
        if elem == 9 or elem == 10:
            dictnotas["h"]+=1
        elif elem == 7 or elem == 8:
            dictnotas["a"]+=1
        else:
            dictnotas["l"]+=1
    returnlist.append(average)
    returnlist.append(dictnotas)
    if dictnotas["h"] > 0 and dictnotas["a"] == 0 and dictnotas["l"] == 0:
        returnlist.append("They did well")
    return returnlist

# Respuesta Felipe
def test2(r):
    avg = round(sum(r)/len(r),3)
    marks = {'h':0,'a':0,'l':0}
    for mark in r:
        if mark>=9:
            marks['h'] +=1
        elif mark<=6:
            marks['l'] +=1
        else:
            marks['a'] +=1
    return [avg, marks] + ["They did well"]*(avg>=9)

print(test(notasa))
print(test(notasb))