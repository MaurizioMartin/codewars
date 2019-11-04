# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:27:14 2019

@author: macl3

URL: https://www.codewars.com/kata/if-you-can-read-this-dot-dot-dot/train/python
    
"""
def to_nato(words):
    dictionary = {'.':'.', '?':'?', '!':'!',' ':'', 'A':'Alfa', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf',"H":"Hotel", 'I':'India', 'J':'Juliett', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}
    phon = [dictionary[w.upper()] for w in words]
    while '' in phon:
        phon.remove('')
    return ' '.join(phon)

print(to_nato('If you can read')) 
# "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta")
