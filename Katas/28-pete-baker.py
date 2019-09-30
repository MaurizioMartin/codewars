# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:29:48 2019

@author: macl3

URL: https://www.codewars.com/kata/pete-the-baker/train/python
"""
def checkAvai(ing,available):
    if ing in available:
        return True
    else:
        return False

def checkNum(num,key,available):
    value = available[key]
    return round(value/num)
    

def cakes(recipe, available):
    lista = [0]*len(recipe)
    for key,value in recipe.items():
        if checkAvai(key,available):
            num = checkNum(value,key,available)
            if num > 0:
                lista[0] = num
                lista.sort()
            else:
                return 0
        else:
            return 0
    return min(lista)

                
    
    
recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available)) # 2, 'Wrong result for example #1')

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe, available)) # 0, 'Wrong result for example #2')