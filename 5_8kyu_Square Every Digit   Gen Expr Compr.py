#Generator expression or comprehension (3rd and 4th example)

"""
Description:
Welcome. In this kata, you are asked to square every digit of a
number and concatenate them.

For example, if we run 9119 through the function, 811181 will
come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""

# Mine / Worked but with bad practices

# def square_digits(num):
#     convert = str(num)
    
#     for i in convert:
#         o = int(i)
#         print(o**2, end='')
# Erased some stuff


# Good practices
# 1
def square_digits(num):
    ansX = ""
    for x in str(num):
        ansX += str(int(x)**2)
        # ansX = ansX + str(int(x)**2)
    return int(ansX)

# 2
def square_digits(num):
    num = str(num)
    ans = ''
    for i in num:
        ans += str(int(i)**2)
    return int(ans)

# 3
def square_digits(num):
    return int(''.join(str(int(x)**2) for x in str(num)))

# 4
def square_digits(num):
    z = ''.join(str(int(i)**2) for i in str(num))
    return int(z)

#The join() method returns a string created by joining
# the elements of an iterable by string separator.

""" 
Generator expressions can be used as function arguments/parameters.
 When used in such a way, the round parentheses can be dropped.
 
 >>> sum(x**2 for x in my_list)
146

>>> max(x**2 for x in my_list)
100
"""