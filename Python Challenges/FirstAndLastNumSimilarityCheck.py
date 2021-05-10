#Exercise 5: Given a list of numbers, return True if first and last number of a list is same

def checkSimilarity(listPara):
    '''Return True if first and last number of a list is same otherwise False'''
    if listPara[0] == listPara[len(listPara) - 1]:
        return True
    else:
        return False

list1 = [10, 20, 30, 40, 10]
list2 = [10, 20, 30, 40, 50]

for i in (list1, list2):
    print("Result is", checkSimilarity(i))

#Expected Output:

#Given list is  [10, 20, 30, 40, 10]
#result is True

#Given list is  [10, 20, 30, 40, 50]
#result is False
