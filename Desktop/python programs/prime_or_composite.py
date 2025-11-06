n = int(input("Enter the number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("The given number is composite.")
            break
    else:
        print("The given number is prime.")
else:
    print("The number is neither prime nor composite.")
