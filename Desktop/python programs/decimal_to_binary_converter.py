num = int(input("Enter the decimal number : "))

def binaryconverter(num):
    global output
    output = ""

    while(num > 0):
        remainder = num % 2
        output += str(remainder)    
        num = num // 2
        

    return output[::-1]

result = binaryconverter(num)
print("The binary equivanlent of decimal {} is : {}".format(num, result))
