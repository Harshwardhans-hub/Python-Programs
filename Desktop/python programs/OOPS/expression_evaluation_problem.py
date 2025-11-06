x = input("Enter the Expression : ")
operator = ["+","-","*","/"]
item = ""
exp = []
for i in x:
	if i in operator :
		exp.append(item)
		exp.append(i)
		item = ""
	else:
		item += i
else:
	exp.append(item)

def check_validity():
    if exp[0] == "" or exp[-1] == "":
        print("Invalid expression")
    elif exp[0] in operator or exp[-1] in operator:
        print("Invalid expression")
    else:
        print("Valid expression")
        
check_validity()




















