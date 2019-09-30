# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:37:29 2019

@author: macl3

URL: https://www.codewars.com/kata/prize-draw/train/python
"""

def rank(st, we, n):
    participants = st.split(",")
    parts = []
    if st == "":
        return "No participants"
    elif len(participants) < n:
        return "Not enough participants"
    else:
        for idx,names in enumerate(participants):
            suma = sum([ord(char) - 96 for char in names.lower()])
            sumalen = len(names)
            sumatotal = (suma + sumalen)*we[idx]
            parts.append((names,sumatotal))
        parts.sort(key=lambda x: (-x[1],x[0]))
        winning = parts[n-1]
        return winning[0]


print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4)) #"Benjamin"
print(rank("Lagon,Lily", [1, 5], 2)) #"Lagon"
print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8)) #"Not enough participants"
print(rank("", [4, 2, 1, 4, 3, 1, 2], 6)) #"No participants"
print(rank("Maurizio,Tinerfe",[5,5],1))

#print([ord(char) - 96 for char in input('Write Text: ').lower()])