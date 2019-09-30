# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:23:59 2019

@author: macl3

URL:https://www.codewars.com/kata/alphabet-war/train/python
"""

left_side = {"w":4, "p":3, "b":2, "s":1}
right_side = {"m":4, "q":3, "d":2, "z":1}

def alphabet_war(fight):

    l_count = sum(left_side[l] for l in fight if l in left_side)
    r_count = sum(right_side[l] for l in fight if l in right_side)

    if l_count > r_count:
        return "Left side wins!"
    elif r_count > l_count:
        return "Right side wins!"
    else:
        return "Let's fight again!"

def alphabet_war2(fight):
    d = {'w':4,'p':3,'b':2,'s':1,
         'm':-4,'q':-3,'d':-2,'z':-1}
    r = sum(d[c] for c in fight if c in d)
    
    return {r==0:"Let's fight again!",
            r>0:"Left side wins!",
            r<0:"Right side wins!"
            }[True]
    
    
print(alphabet_war("z"))
print(alphabet_war("zdqmwpbs"))
print(alphabet_war("zzzzs"))
print(alphabet_war("wwwwwwz"))