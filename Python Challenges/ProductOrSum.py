#Exercise 1: Given two integer numbers return their product. If the product is greater than 1000, then return their sum

def productOrSum(num1, num2):
    product = num1 * num2
    if product > 1000:
        return num1 + num2
    else:
        return product
        
num1 = int(input("number1 = "))
num2 = int(input("number2 = "))

print("The result is", productOrSum(num1, num2))

#Output:
#number1 = 20
#number2 = 30
#The result is 600
