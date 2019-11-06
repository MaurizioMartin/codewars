# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:14:14 2019

@author: macl3

URL: https://www.codewars.com/kata/decode-the-morse-code/train/python
"""
def checkLetter(word):
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
       'C':'-.-.', 'D':'-..', 'E':'.',
       'F':'..-.', 'G':'--.', 'H':'....',
       'I':'..', 'J':'.---', 'K':'-.-',
       'L':'.-..', 'M':'--', 'N':'-.',
       'O':'---', 'P':'.--.', 'Q':'--.-',
       'R':'.-.', 'S':'...', 'T':'-',
       'U':'..-', 'V':'...-', 'W':'.--',
       'X':'-..-', 'Y':'-.--', 'Z':'--..',
       '1':'.----', '2':'..---', '3':'...--',
       '4':'....-', '5':'.....', '6':'-....',
       '7':'--...', '8':'---..', '9':'----.',
       '0':'-----', ', ':'--..--', '.':'.-.-.-',
       '?':'..--..', '/':'-..-.', '-':'-....-',
       '(':'-.--.', ')':'-.--.-', '!':'-.-.--',
       'SOS':'...---...'
    }
    word = [k for k, v in MORSE_CODE_DICT.items() if word == v]
    if word:
        return word[0]

    
def decodeMorse(morse_code): 
    morse_code = morse_code.strip()
    morse_words = morse_code.split(' ')
    word = ""
    for words in morse_words:
        if words == "":
            word += " "
        else:
            word += checkLetter(words)         
    
    return word.replace("  "," ")


print(decodeMorse('.... . -.--   .--- ..- -.. .'))
