#Problem Title: Anagrams

#Problem:
#Two strings are anagrams if you can make one from the other by rearranging the letters.

#Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are 
#anagrams, and False otherwise.

#For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return 
#False.

#Solution:
def addAscii(string):
    result = 0
    for char in string:
        result += ord(char)
    return result
    
def is_anagram(str1, str2):
    if addAscii(str1) == addAscii(str2):
        return True
    return False
