# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:25:34 2019

@author: macl3

URL: 
"""
class Dinglemouse(object):
    
    def __init__(self):
        self.name = None
        self.sex  = None
        self.age  = None
        self.salute = {'hello':'Hello.'}
    
    def setAge(self, age):
        self.age = age
        self.salute['age']='I am {}.'.format(self.age)
        return self
        
    def setSex(self, sex):
        self.sex = sex
        self.salute['sex']='I am {}.'.format("male" if self.sex=='M' else "female")
        return self
        
    def setName(self, name):
        self.name = name
        self.salute['name']='My name is {}.'.format(self.name)
        return self
        
    def hello(self):
        return ' '.join(self.salute.values())
    


dm = Dinglemouse().setName("Bob").setAge(27).setSex('M')
#expected = "Hello. My name is Bob. I am 27. I am male."
print(dm.hello())
dm2 = Dinglemouse().setName("Alice").setSex('F')
#expected = "Hello. My name is Alice. I am female."
print(dm2.hello())
