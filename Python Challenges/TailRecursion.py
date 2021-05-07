#In this code, i used Tail-recursion to find the length of the string 

def findLength(value, itr = 0):
    if value == '':
        return itr
    else:
        return findLength(value[1:], itr + 1)
        
text = "Godavari"
print("Length of string {}: {}".format(text, findLength(text)))    

#Output :
#Length of string Godavari: 8  

