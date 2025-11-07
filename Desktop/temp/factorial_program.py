# Python script to find the factorial of a user-defined number

n = int(input("Enter the number whose factorial is required : "))
factorial = 1
for i in range(1, n + 1):  
    factorial *= i

print("The factorial of {} is : {}".format(n, factorial))
