def lower_case(user_str):
	return user_str.lower()	

def upper_case(user_str):
	return user_str.upper()	

def sentence_case(user_str):
	temp_result = ""
	for i in range(len(user_str)):
		if i == 0:
			temp_result = user_str[i].upper()
		else :
			temp_result = temp_result + user_str[i].lower()
	return temp_result

def capitalise_case(user_str):
	x = user_str.split(" ")
	final_result = ""

	for i in x :
		temp_result = ""
		for j in range(len(i)):
			if j==0 :
				temp_result = i[j].upper()
			else :
				temp_result = temp_result + i[j].lower()

		if final_result == "":
			final_result = temp_result
		else :
			final_result = final_result + " " + temp_result

	return final_result

def toggle_case(user_str):
	temp_result = ""
	for i in user_str :
		if i.isupper():
			temp_result = temp_result + i.lower()
		else : 
			temp_result = temp_result + i.upper()
	return temp_result

user_str = input("Enter Your String : ")
choice = int(input("Press 1 for Lower Case\nPress 2 for Upper Case\nPress 3 for Sentence Case\nPress 4 for Capitalise Case\nPress 5 for Toggle Case\nPlease enter a valid Choice : "))
if choice == 1 : 
	converted_str = lower_case(user_str)
	print("User String : ",user_str)
	print("After Conversion")
	print("Converted String : ",converted_str)
elif choice == 2 : 
	converted_str = upper_case(user_str)
	print("User String : ",user_str)
	print("After Conversion")
	print("Converted String : ",converted_str)
elif choice == 3 : 
	converted_str = sentence_case(user_str)
	print("User String : ",user_str)
	print("After Conversion")
	print("Converted String : ",converted_str)
elif choice == 4 : 
	converted_str = capitalise_case(user_str)
	print("User String : ",user_str)
	print("After Conversion")
	print("Converted String : ",converted_str)
elif choice == 5 : 
	converted_str = toggle_case(user_str)
	print("User String : ",user_str)
	print("After Conversion")
	print("Converted String : ",converted_str)
else:
	print("Invalid Choice. Please Re-enter your choice.")