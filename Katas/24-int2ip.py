# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:27:33 2019

@author: macl3

URL: https://www.codewars.com/kata/int32-to-ipv4/train/python
"""
import ipaddress

def int32_to_ip1(int32):
    return str(ipaddress.IPv4Address(int32))


#second solution
   
    
# convert binary
def convert_bin(arr):
  suma = 0
  for x,y in enumerate(arr[::-1]):
    suma = suma + 2**x * int(y)
  return suma
  
def int32_to_ip(int32):

  n = ""

  while int32 > 0:
    y = str(int32 % 2)
    n = y + n
    int32 = int(int32 / 2)


  if len(n) != 32: # make 32 bit
    while len(n) != 32:
      n = '0' + n

  a = n[:8] # first 8
  b = n[8:16] # secound 8
  c = n[16 : 24] # third 8
  d = n[24 : 32] # fourth 8

  return(str(convert_bin(a))+'.'+str(convert_bin(b))+'.'+str(convert_bin(c))+'.'+str(convert_bin(d)))
  
print(int32_to_ip(2154959208)) #"128.114.17.104") 
print(int32_to_ip(0)) # "0.0.0.0")
print(int32_to_ip(2149583361)) #"128.32.10.1")

