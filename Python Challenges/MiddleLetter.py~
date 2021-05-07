#Problem Name: Middle letter

#Problem Statement:

#Write a function named mid that takes a string as 
#its parameter. Your function should extract and 
#return the middle letter. If there is no middle 
#letter, your function should return the empty string.

#For example, mid("abc") should return "b" and 
#mid("aaaa") should return "".

#Solution:

def mid(text):
    '''return middle character of string if the string is odd otherwise empty string is returned.'''

    textLength = len(text)
    last = textLength - 1
    
    for i in range(0, textLength):    
        if i == last:
            return text[i]
        elif last > 0:
            last -= 1
        else:
            return ''
    
    
    #if textlength % 2 != 0:
    #    return text[textlength // 2]
    #return ""
    
print(mid("abc"))
print(mid("aaaa"))


#Output:
#b
#

