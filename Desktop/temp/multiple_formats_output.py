
def sentence_case(a):

	n = ""
	for i in range(len(a)):
		
		n = a[0].upper()
		if a[i] == "." and a[i] == "." :
			n= a[i+1].upper()
			n.append(i)

		return n

for i in range(len(a)):

	if b == 1:
		x = a.upper()
		print(x)
		break

	elif b == 2:
		y = a.lower()
		print(y)
		break

	elif b == 3:	
		result = sentence_case(a)
		print(result)
		break



a = input("Enter a string : ")
print("Enter '1 for Uppercase , '2' for Lowercase , '3' for First letter capital, '4' for Toggle and '5'for Sentence case")
b = int(input("Enter the choice : "))


