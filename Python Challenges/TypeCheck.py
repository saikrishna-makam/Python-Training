#Problem Title: Type check

#Problem:

#Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and 
#False otherwise.

#For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

#Solution:

def only_ints(par1, par2):
    '''Return True if both parameters are integers, and False otherwise.'''
    return type(par1) == int and type(par2) == int
    
print(only_ints(1, 2))
print(only_ints("a", 1))

#Output:
#True
#False