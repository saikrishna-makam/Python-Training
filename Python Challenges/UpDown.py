#Problem Title: Up and down
#Problem:
#Define a function named up_down that takes a single number as its parameter. Your function return a tuple containing two numbers; 
#the first should be one lower than the parameter, and the second should be one higher.

#For example, calling up_down(5) should return (4, 6).

#Solution:

def up_down(val):
    return (val - 1, val + 1)
