# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 09:27:51 2019

@author: macl3

URL:https://www.codewars.com/kata/sql-basics-monsters-using-case/train/sql
"""

SELECT top_half.id, heads, legs, arms, tails,
CASE WHEN heads > arms or tails > legs THEN 'BEAST'
ELSE 'WEIRDO'
END AS species
FROM top_half
LEFT JOIN bottom_half
ON top_half.id = bottom_half.id
ORDER BY species;