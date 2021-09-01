"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

def descending_order(num):
    # Bust a move right here
"""

def descending_order(num):
    num = sorted([i for i in str(num)], reverse=True)
    num = "".join(num)
    return int(num)
#sorted takes a list as the 1 param
#Join takes all items in an iterable and joins them into a string. The separator
    #must be string --->  "".join

def descending_order(num):
    return int("".join(sorted([i for i in str(num)], reverse=True)))
