# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:29:06 2019

@author: macl3

URL: https://www.codewars.com/kata/user-class-for-banking-system/train/python
"""

class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    #Happy coding
    
    def withdraw(self, monWithdraw):
        if self.balance - monWithdraw < 0:
            raise ValueError
        else:
            self.balance -= monWithdraw
            return "{} has {}.".format(self.name, str(int(self.balance)))
            
    def check(self, name, money):
        if not name.checking_account:
            raise ValueError
        name.withdraw(money)
        self.add_cash(money)
        return "{} has {} and {} has {}.".format(self.name, self.balance, name.name, name.balance)
        
    def add_cash(self, money):
        self.balance += money
        return "{} has {}.".format(self.name, str(int(self.balance)))
    

Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)

print(Joe.withdraw(50)) # Returns 'Jeff has 68.'

print(Joe.check(Jeff, 50)) # Returns 'Joe has 120 and Jeff has 18.'



#print(Jeff.check(Joe, 80)) # Raises a ValueError

Joe.checking_account = True # Enables checking for Joe

print(Jeff.check(Joe, 80)) # Returns 'Jeff has 98 and Joe has 40'

#print(Joe.check(Jeff, 100)) # Raises a ValueError

print(Jeff.add_cash(20.00)) # Returns 'Jeff has 118.'