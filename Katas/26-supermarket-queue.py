# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:30:21 2019

@author: macl3
URL: https://www.codewars.com/kata/the-supermarket-queue/train/python
"""

def queue_time(customers, n):
    queue = [0]*n
    if n == 1:
        return sum(customers)
    else:
        for cust in customers:
            queue[0] += cust
            queue.sort()
        return max(queue)


print(queue_time([], 1)) # 0, "wrong answer for case with an empty queue")
print(queue_time([5], 1)) #5, "wrong answer for a single person in the queue")
print(queue_time([2], 5)) #2, "wrong answer for a single person in the queue")
print(queue_time([1,2,3,4,5], 1)) # 15, "wrong answer for a single till")
print(queue_time([1,2,3,4,5], 100)) # 5, "wrong answer for a case with a large number of tills")
print(queue_time([2,2,3,3,4,4], 2)) # 9, "wrong answer for a case with two tills")