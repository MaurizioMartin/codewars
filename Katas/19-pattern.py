# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:26:15 2019

@author: macl3

URL: https://www.codewars.com/kata/complete-the-table-pattern/train/python
"""

def pattern(rows, columns, s):
    string = []
    s = [e for e in s]
    for i in range(rows):
        string.append('+---+')
        for j in range(columns-1):
            string.append('---+')
        string.append('\n|')
        for j in range(columns):
            if len(s) != 0: 
                string.append(' '+s[0]+' |')
                del s[0]
            else:
                string.append('   |')
        string.append("\n")
    for j in range(columns):
        string.append('+---')
    string.append("+")
    return "".join(string)

def patternNacho(rows, columns, s):
    d = rows*columns
    s += " "*(d-len(s))
    res = "+---"*columns+"+\n"
    for i in range(len(s)):
      if i%columns==(columns-1) and i!=len(s)-1:
        res += "| "+s[i]+" |\n"+"+---"*columns+"+\n"
      elif i%columns==(columns-1) and i==len(s)-1:
        res += "| "+s[i]+" |\n"+"+---"*columns+"+"
      else:
        res += "| "+s[i]+" "
      
    return res


print(pattern(4,4,"hello world!"))
print(pattern(3, 3, "codewars"))
print(pattern(3, 4, "Nice pattern"))
print(pattern(4, 3, "Nice pattern"))