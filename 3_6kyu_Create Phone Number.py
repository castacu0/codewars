
"""
Write a function that accepts an array of 10 integers
(between 0 and 9), that returns a string of those numbers
in the form of a phone number.

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) 
# => returns "(123) 456-7890"


The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
"""
# My try

# def create_phone_number(n):
#     lol = "".join(map(str, n[0:5]))
#     parentheses = "".join(map(str, n[0:3]) )
#     three = "".join(map(str, n[3:6]) )
#     four = "".join(map(str, n[6:10]) )
#     return "("+ parentheses +") "+ three +"-"+ four + "   NEW: " + lol

# Best Practices
#1
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

#2
def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

#3
def create_phone_number(n):
    m = ''.join(map(str, n))
    return f"({m[:3]}) {m[3:6]}-{m[6:]}"

#4
create_phone_number = lambda n: f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

#5
def create_phone_number(n):
  str1 =  ''.join(str(x) for x in n[0:3])
  str2 =  ''.join(str(x) for x in n[3:6])
  str3 =  ''.join(str(x) for x in n[6:10])

  return '({}) {}-{}'.format(str1, str2, str3) #or
  return f'({str1}) {str2}-{str3}'