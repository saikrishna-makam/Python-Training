#Exercise 12: Calculate income tax for the given income by adhering to the below rules
#Taxable Income	Rate (in %)
#First $10,000	0
#Next $10,000	10
#The remaining	20

def calculateIncomeTax(income):
    '''Return the income tax for the income by adhering to the given rules'''
    if income <= 10000:
        return 0
    elif income <= 20000:
        return ((income - 10000) * 0.1);
    else: 
        return (10000 * 0.1) + ((income - 20000) * 0.2) 

print("Total income tax payable is $", int(calculateIncomeTax(45000)))


#Expected Output:

#For example, suppose that the taxable income is $45000 the income tax payable is

#$10000*0% + $10000*10%  + $25000*20% = $6000.
