# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 09:29:55 2019

@author: macl3

URL: 
    
"""

from bs4 import BeautifulSoup
import requests

def get_member_since(username):
    url = "https://www.codewars.com/users/" + username
    page = requests.get(url)
    html = BeautifulSoup(page.text, "html.parser")
    divs = html.find_all("div", class_="stat")
    for div in divs:
        if "Member " in div.text:
            return div.text.split(":")[-1]
            
    

print(get_member_since("jhoffner"))