"""

Your task is to write a function which returns the 
sum of following series upto nth term(parameters).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Rules:
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return 0.00

You will only be given Natural Numbers as arguments.

Examples:
SeriesSum(1) => 1 = "1.00"
SeriesSum(2) => 1 + 1/4 = "1.25"
SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"
                


"""

def series_sum(n): #let's use 2
                              
    #return '{0:.2f}'.format(sum(1/(3 * i + 1) for i in range(n)))
    # the 0 is the value or the thing I want to modify
    return (f"{sum (1.00/(3 * i + 1) for i in range(n)):.2f}")
    

#series_sum(0)
series_sum(1) # 1 is not being counted
series_sum(2) # 2 is not being counted

# Ok, so explanation.
# For each i in the range(from 0 to the number[in this case 2])
# range(start=0, stop, step=1)
# The number 2 is excluded

# Return 3 times i plus 1 in the Generator expression. So

# i=0 >>> 3 times 0 = 0 + 1 = 1   and 1 / 1 = 1
# Next
# i=1 >>> 3 times 1 = 3 + 1 = 4   and 1 / 4 = 0.25   or 1/4
# Next
# >>>   THIS ITERATION IS NOT INCLUDED: because i=2 >>> 3 times 2 = 6 + 1 = 7 and 1 / 7 = 0.14

# The results from every iteration, sum them all.

# Then return it inside of '{0:.2f}'
          # 0 means the argument by its index (In other words, the first arg passed)
          # : this is the separator
          # .2 is the number of decimals needed
          # f means it will cast is as float


#BEST PRECTICES
#1
def series_sum(n):
    return '{0:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

#2
def series_sum(n):
    sum = 0.0
    for i in range(0,n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum 

#3
def series_sum(n):
    return '%.2f' % sum(1.0 / i for i in xrange(1, 3 * n, 3))

