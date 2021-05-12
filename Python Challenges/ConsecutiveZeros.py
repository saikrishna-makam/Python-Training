#Problem Title: Consecutive zeros

#Problem:

#The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest 
#number of consecutive zeros in the string. For example, given the string:

#"1001101000110"
#The biggest number of consecutive zeros is 3.

#Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function 
#should return the number described above.


#Solution:

def consecutive_zeros(binary):
    maxZeroCount = 0
    zeroCount = 0
    lastNum = 0
    for num in binary:
        if num == '0':
            zeroCount += 1
            if maxZeroCount < zeroCount:
                maxZeroCount = zeroCount
        else:
            zeroCount = 0
    return maxZeroCount
