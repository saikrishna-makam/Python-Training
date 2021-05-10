#Exercise 4: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new 
#string
#For example, removeChars("pynative", 4) so output must be tive.

def removeChars(string, n):
    '''Return a new resulted string by removing characters from a string starting from zero up to n'''
    return [string[i] for i in range(n, len(string))]
        
print("".join(removeChars("pynative", 4)))

#Output:
#tive
