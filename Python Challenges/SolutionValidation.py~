#Problem Title: Solution validation

#Problem:

#The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too 
#hard.

#Write a function named validate that takes code represented as a string as its only parameter.

#Your function should check a few things:

#the code must contain the def keyword
#otherwise return "missing def"
#the code must contain the : symbol
#otherwise return "missing :"
#the code must contain ( and ) for the parameter list
#otherwise return "missing paren"
#the code must not contain ()
#otherwise return "missing param"
#the code must contain four spaces for indentation
#otherwise return "missing indent"
#the code must contain validate
#otherwise return "wrong name"
#the code must contain a return statement
#otherwise return "missing return"
#If all these conditions are satisfied, your code should return True.

#Here comes the twist: your solution must return True when validating itself.


#Solution:

def validate(codeString):
    if not "def" in codeString:
        return "missing def"
    elif not ":" in codeString:
        return "missing :"
    elif not ("(" in codeString and ")" in codeString):
        return "missing paren"
    elif "(" + ")" in codeString:
        return "missing param"
    elif not "    " in codeString:
        return "missing indent"
    elif not "validate" in codeString:
        return "wrong name"
    elif not "return" in codeString:
        return "missing return"
    return True
