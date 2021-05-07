#Problem Name: Capital indexes

#Problem Statement:

#Write a function named capital_indexes. The function 
#takes a single parameter, which is a string. Your 
#function should return a list of all the indexes in 
#the string that have capital letters.

#For example, calling capital_indexes("HeLlO") should 
#return the list [0, 2, 4].

#Solution :

def capital_indexes(value):
    list = []
    for i in range(0, len(value)):
        if value[i].isupper():
            list.append(i)
    return list
    
capital_indexes("HeLlO")

#Output:
#[0, 2, 4]

