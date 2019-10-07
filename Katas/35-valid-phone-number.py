# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:29:28 2019

@author: macl3

URL: https://www.codewars.com/kata/valid-phone-number/train/python
    
"""
import re

def validPhoneNumber(phoneNumber):
    return True if re.search("^\([\d]{3}\)[ ][\d]{3}[-][\d]{4}$", phoneNumber) else False
    
print(validPhoneNumber("(123) 456-7890")) #  =>  returns true
print(validPhoneNumber("(1111)555 2345")) #  => returns false
print(validPhoneNumber("(098) 123 4567")) #  => returns false
print(validPhoneNumber("(123) 456-7890abc")) # => returns false