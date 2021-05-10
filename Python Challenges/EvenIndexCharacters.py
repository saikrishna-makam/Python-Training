#Exercise 3: Given a string, display only those characters which are present at an even index number.
#For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

str = "pynative"
evenList = [str[i] for i in range(0, len(str)) if i % 2 == 0]
print("Printing only even index chars")
for char in evenList:
    print(char)

#Expected Output:

#Orginal String is  pynative
#Printing only even index chars
#p
#n
#t
#v
