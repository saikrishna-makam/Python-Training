#Exercise 9: Reverse a given number and return true if it is the same as the original number

def toReverse(string):
    '''Return reverse string of passed string'''
    return string[::-1]
    
num1 = 121
num2 = 125

strnum1 = str(num1)
strnum2 = str(num2)

def checkPelindrome(str1):
    '''Check whether the number is Pelindrome number or not'''
    if str1 == toReverse(str1):
        print("The original and reverse number is the same")
    else:
        print("The original and reverse number is not same")

checkPelindrome(strnum1)
checkPelindrome(strnum2)

  
#Expected Output:

#original number 121
#The original and reverse number is the same

#original number 125
#The original and reverse number is not same
