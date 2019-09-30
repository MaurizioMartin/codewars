# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:34:56 2019

@author: macl3

URL: https://www.codewars.com/kata/80-s-kids-number-2-help-alf-find-his-spaceship/train/python
"""

def find_spaceship(astromap):
    astromap = astromap[::-1]
    splitted = astromap.split("\n")
    y=0
    for punto in splitted:
        if len(splitted)  == 1:
            print(len(punto))
            x=(len(punto)-1)
            for pun in punto:
                if pun == 'X':
                    return [x,y]
                else:
                    y+=1
            return("Spaceship lost forever.")
        else:
            x=(len(punto))
            for pun in punto:
                if pun == 'X':
                    x-=1
                    return [x,y]
                elif pun == '.':                  
                    x-=1
                    if x == 0:
                        x= len(punto)-1
                        y+=1
    return ("Spaceship lost forever.")
            
   
def find_spaceship2(astromap):
    if 'x' not in astromap:
        return ("Spaceship lost forever.")
    x = astromap.split("\n")
    x.reverse()
    coord = [(elm,i) for i in range(len(x)) for elm in range(len(x[i])) if x[i][elm] == "X"]
    coordinates = [y for x in coord for y in x]
    return coordinates                    

def find_spaceship3(astromap):
    for y, x in enumerate(reversed(astromap.split('\n'))):
        if 'X' in x:
            return [x.index('X'), y]
        else:
            return ("Spaceship lost forever.")
        
print(find_spaceship("X\n."))       
print(find_spaceship("X"))
print(find_spaceship("..........\n..........\n.......X..\n..........\n.........."))
print(find_spaceship("........................"))
print(find_spaceship("\n\n\n\n"))
print(find_spaceship(".X."))