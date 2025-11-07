# Python script to find the factorial of a user-defined number using a while loop

n = int(input("Enter the number whose factorial is required : "))
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print("The factorial of {} is : {}".format(n, factorial))
