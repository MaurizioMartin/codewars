# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:30:06 2019

@author: macl3

URL: https://www.codewars.com/kata/street-fighter-2-character-selection/train/python
"""

def street_fighter_selection(fighters,initial_position,moves):
    position = list(initial_position)
    result = []
    for mov in moves:
        if mov == "up":
            position[0] = 0
        elif mov == "down":
            position[0] = 1
        elif mov == "left":
            position[1] = (position[1]-1)%6
        elif mov == "right":
            position[1] = (position[1]+1)%6
        result.append(fighters[position[0]][position[1]])
    print(result)
    return result
    
fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
moves =  ["right"]*8
initial_position = (0,0)
street_fighter_selection(fighters,initial_position,moves)
# ['E.Honda', 'Blanka', 'Guile', 'Balrog', 'Vega', 'Ryu', 'E.Honda', 'Blanka']
moves =  ["left"]*8
street_fighter_selection(fighters,initial_position,moves)
# ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog']

moves =  ["up"]*4
street_fighter_selection(fighters,initial_position,moves)
moves =  ["down","right","up","left"]*2
street_fighter_selection(fighters,initial_position,moves)
#solution = ['Ken', 'Chun Li', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'E.Honda', 'Ryu']