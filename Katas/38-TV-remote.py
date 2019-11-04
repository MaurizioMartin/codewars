# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:08:14 2019

@author: macl3

URL: https://www.codewars.com/kata/tv-remote-wrap/train/python
"""

graph = {
        #["a","b","c","d","e","1","2","3"]
        'a': ['3', '#', 'f', 'b'],
        'b': ['a', 'g', 'c','-'],
        'c': ['b', 'h', 'd', '!'],
        'd': ['c', 'i', 'e', '$'],
        'e': ['d', 'j', '1', '%'],
        '1': ['e', '4', '2', '&'],
        '2': ['1', '5', '3', '('],
        '3': ['2', '6', 'a', ')'],
        #["f","g","h","i","j","4","5","6"]
        'f': ['6', 'a', 'g', 'k'],
        'g': ['f', 'b', 'h', 'l'],
        'h': ['g', 'c', 'm', 'i'],
        'i': ['h', 'd', 'j', 'n'],
        'j': ['i', 'e', '4', 'o'],
        '4': ['j', '1', '5', '7'],
        '5': ['4', '2', '8', '6'],
        '6': ['5', '3', '9', 'f'],
        #["k","l","m","n","o","7","8","9"]
        'k': ['f', 'l', 'p', '9'],
        'l': ['k', 'g', 'q', 'm'],
        'm': ['l', 'h', 'r', 'n'],
        'n': ['m', 'i', 's', 'o'],
        'o': ['n', 'j', 't', '7'],
        '7': ['o', '4', '.', '8'],
        '8': ['7', '5', '@', '9'],
        '9': ['8', '6', '0', 'k'],
        #["p","q","r","s","t",".","@","0"]
        'p': ['0', 'k', 'u', 'q'],
        'q': ['p', 'l', 'v', 'r'],
        'r': ['q', 'm', 'w', 's'],
        's': ['r', 'n', 'x', 't'],
        't': ['s', 'o', 'y', '.'],
        '.': ['t', '7', 'z', '@'],
        '@': ['.', '8', '_', '0'],
        '0': ['@', '9', '/', 'p'],
        #["u","v","w","x","y","z","_","/"]
        'u': ['/', 'p', '#', 'v'],
        'v': ['u', 'q', '-', 'w'],
        'w': ['v', 'r', '!', 'x'],
        'x': ['w', 's', '$', 'y'],
        'y': ['x', 't', '%', 'z'],
        'z': ['y', '.', '&', '_'],
        '_': ['z', '@', '(', '/'],
        '/': ['_', '0', ')', 'u'],
        #["aA","SP"," "," "," "," "," "," "]
        '#': [')', 'u', 'a', '-'],
        '-': ['#', 'v', 'b', '!'],
        '!': ['-', 'w', 'c', '$'],
        '$': ['!', 'x', 'd', '%'],
        '%': ['$', 'y', 'e', '&'],
        '&': ['%', 'z', '1', '('],
        '(': ['&', '_', '2', ')'],
        ')': ['(', '/', '3', '#']
        }

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

def getSuma(words):
    suma = 0
    for w in range(len(words)):
        if w < len(words)-1:
            x = bfs(graph,words[w],words[w+1])
            suma += len(x)
    return suma

def iter_starting_at(start_pos, string):
    for i in range(start_pos, len(string)):
        yield string[i]

def tv_remote(words):
    words = words.replace(' ','-')
    words = "a"+words
    mayus = False
    lista = []
    for w in iter_starting_at(0, words):
        if w.isupper() and mayus == False:
            lista.append('#'+w.lower())
            mayus = True
        elif w.isupper() and mayus == True:
            lista.append(w.lower())
        elif w.islower() and mayus == True:
            lista.append('#'+w.lower())
            mayus = False
        else:
            lista.append(w)
    return getSuma("".join(lista))  

        
        
#lower
print(tv_remote("does")) #     16
print(tv_remote("your")) #     21
#Upper
print(tv_remote("DOES")) #     19
print(tv_remote("YOUR")) #     22
#Code
print(tv_remote("Code")) #     24

#with spaces
print(tv_remote("Code Wars")) #49
print(tv_remote("The-Quick-Brown-Fox-Jumps-Over-A-Lazy-Dog.")) #254
print(tv_remote("eDp W_lN7wPbj")) #92
print(tv_remote("18Z")) #19
