"""
In this simple assignment you are given a number and
have to make it negative. But maybe the number is already negative?

Example:

make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
Notes:

The number can be negative already, in which case no
change is required.
Zero (0) is not checked for any specific sign. Negative
zeros make no mathematical sense.
"""


#It worked
def make_negative( number ):
    if number > 0:
        return -(number)
    elif number == 0:
        return number
    else:
        return number

#Best practices
#1
def make_negative( number ):
    return -abs(number)
    # Absolute value of a number is the value without considering
    # its sign. Hence absolute of 10 is 10, -10 is also 10.

    # The abs() takes only one argument

#2
def make_negative( number ):
    return -number if number > 0 else number
    return number if number <= 0 else -number