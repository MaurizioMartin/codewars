# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:22:32 2019

@author: macl3

URL: https://www.codewars.com/kata/sql-with-sailor-moon-thinking-about-joins-dot-dot-dot/train/sql
"""

SELECT ss.senshi_name as "sailor_senshi", ss.real_name_jpn as "real_name", c.name as "cat", sc.school as "school"
FROM sailorsenshi as ss
LEFT JOIN cats as c
ON ss.cat_id = c.id
LEFT JOIN schools as sc
ON ss.school_id = sc.id;