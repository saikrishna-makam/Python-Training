#Problem Title: All equal

#Problem:

#Define a function named all_equal that takes a list and checks whether all elements in the list are the same.
#For example, calling all_equal([1, 1, 1]) should return True.

#Solution:

def all_equal(list):
    return len([val for val in list if list[0] == val]) == len(list)
