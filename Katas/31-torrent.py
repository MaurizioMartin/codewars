# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:24:27 2019

@author: macl3

URL: https://www.codewars.com/kata/computer-problem-series-number-2-torrent-download/train/python
"""
def torrent(files): 
    lista = []
    lista2 = []
    for file in files:
        data = file["size_GB"]*1000
        speed = file["speed_Mbps"]
        cont = int(data/speed*8)       
        lista.append((file["name"],cont))
    lista.sort(key = lambda x: (x[1],x[0])) 
    for lis in lista:
        lista2.append(lis[0])
    return lista2,lista[-1][1]
            
            


file_1 = {"name": "alien", "size_GB": 38, "speed_Mbps": 38}
file_2 = {"name": "predator", "size_GB": 38, "speed_Mbps": 2}
file_3 = {"name": "terminator", "size_GB": 5, "speed_Mbps": 25}
file_4 = {"name": "zombieland", "size_GB": 38, "speed_Mbps": 38}

print(torrent([file_1, file_4])) # -> ["alien", "zombieland"], 8000

print(torrent([file_1, file_2, file_3])) #-> ["terminator", "alien", "predator"], 152000