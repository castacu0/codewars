"""
Write a program that finds the summation of every number
from 1 to num. The number will always be a positive integer
greater than 0.
"""
# Again, I was missing the Return
def summation(num): #3
    sumX = 0 
    for i in range(1, num + 1): 
        sumX = sumX + i
    return sumX
summation(8)
        
# Best practices
# 1 / Faster
def summation(num):
    return (num + 1) * num / 2

# 2 Clever
def summation(num):
    return sum(range(1, num+1))
    
