#Problem Title: Thousands separator

#Problem:

#Write a function named format_number that takes a non-negative number as its only parameter.

#Your function should convert the number to a string and add commas as a thousands separator.

#For example, calling format_number(1000000) should return "1,000,000".

#Solution:

def format_number(number):
    strNumber = str(number)
    result = ""
    count = 0
    for i in range(len(strNumber) - 1, -1, -1):
        result = result + strNumber[i]
        count += 1
        if (i - 1) >= 0 and count % 3 == 0:
            result = result + ","
    return result[::-1]
