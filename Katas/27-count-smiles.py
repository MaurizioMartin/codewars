# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:32:45 2019

@author: macl3

URL: https://www.codewars.com/kata/count-the-smiley-faces/train/python
"""
import re
def count_smileys(arr):
    r = re.compile("[:|;][-|~]?[)|D]")
    matches = list(filter(r.match, arr))
    return len(matches)
    



print(count_smileys([])) # 0)
print(count_smileys([':D',':~)',';~D',':)'])) # 4)
print(count_smileys([':)',':(',':D',':O',':;'])) # 2)
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))# 1)
