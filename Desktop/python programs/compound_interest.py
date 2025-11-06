#Compound interest calculator
Principal_amount = int(input("Enter the amount : "))
Rate_of_interest = float(input("Enter the rate of interest :" ))
Tenure = int(input("Enter the tenure/time period : "))
n = int(input("Enter the number of times interest should be compounded : "))

Final_amount = Principal_amount * (1 + Rate_of_interest/n) ** (n * Tenure)
print("The compound interest is : {}".format(Final_amount))