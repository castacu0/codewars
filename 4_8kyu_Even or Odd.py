#My try / Worked
def even_or_odd(number):
    try:
        if number % 2 == 0:
            return "Even"
        else:   
            return "Odd"
    except EOFError as e:
        print(e)
        
even_or_odd(17)

#Better Practices
#1st
def even_or_odd(number):
    return 'Even' if number % 2 else 'Odd'


#2nd 👑 Clever
def even_or_odd(number):
  return ["Even", "Odd"][number % 2]
        #There's an array, consisting of two strings, "Even" and "Odd".
        #The first one thefore has index of 0 and the second has index of 1.
        #number % 2 is 1 for odd numbers and 0 for even numbers.
        #Therefore this expression return the string "Even"
        # for even numbers and "Odd" for odd numbers."""


#3rd
def even_or_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"