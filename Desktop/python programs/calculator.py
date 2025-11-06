def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        print("Division by zero is not possible")
        return None
    else:
        return n1 / n2

def typeconverter(result):
    if result % 1 == 0:
        return int(result)
    else:
        return result

def calculator():
    while True:
        n1 = int(input("Enter first number : "))
        n2 = int(input("Enter second number : "))
        print("Which operation you would like to perform?")
        print("Press 1 for Addition, 2 for Subtraction, 3 for Multiplication, and 4 for Division")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            result = add(n1, n2)
        elif choice == 2:
            result = sub(n1, n2)
        elif choice == 3:
            result = mul(n1, n2)
        elif choice == 4:
            result = div(n1, n2)
        else:
            print("Wrong input") 
            continue

            print("Result = {}".format(typeconverter(result)))
    calculator()

        repeat = input("Would you like to continue using the calculator? : ")
        if repeat != 'yes':
            break

calculator()
