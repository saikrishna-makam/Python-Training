#Exercise 11: Write a code to extract each digit from an integer, in the reverse order

val = 7536

while(val > 0):
    print(val % 10, end=" ")
    val //= 10
    
#Expected Output:

#If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
