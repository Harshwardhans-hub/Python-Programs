def create_contact():
	name = input("Enter the name : ")
	contact = input("Enter the contact details : ")
	email = input("Enter the email : ")
	contact_entry = "{},{},{}\n".format(name,contact,email)
	file1 = open("details.txt","a")
	file1.write(contact_entry)
	file1.close()
	print("Contact Added Successfully.")

def display_contact(x):
	x = x.replace("\n","")
	contact = x.split(",")
	print("Name :",contact[0])
	print("Email :",contact[2])
	print("Phone_Number:",contact[1])

def read_data():
	file1 = open("details.txt","r")
	result = file1.readlines()	
	file1.close()
	return result 

def write_data(result):
	file = open("details.txt","w")
	for i in result:
		file.write(i)
	file.close()



def display_all_contact():
	result = read_data()
	#print("All Contact Details : ",result)
	print("==============================")
	for i in result : 
		#print(i)
		i = i.replace("\n","")
		#print(i)
		contact_detail = i.split(",")
		#print(contact_detail)
		print("Name : ",contact_detail[0])
		print("Contact : ",contact_detail[1])
		print("Email : ",contact_detail[2])
		print("==============================")

def search_contact():
	search = input("Enter the Search Element : ")
	result = read_data()
	for i in result:
		i = i.replace("\n","")
		contact_detail = i.split(",")
		if search in contact_detail	:
			print("Contact Found Succesfully.")
			print("==============================")
			display_contact(i)
			print("==============================")
			return i,result,contact_detail
			break	
	else:
		print("Contact details not found.")


def update_choice_selection():
	update_choice = input("Press 1 to change Name\nPress 2 to change Email\nPress 3 to change Contact No\nPlease enter a valid input")
	if update_choice == "1":
		new_name = input("Enter New Name : ")
		updated_contact[0] = new_name

	elif update_choice == "2":
		new_email = input("Enter New Email : ")
		updated_contact[1] = new_email

	elif update_choice == "3":
		new_number = input("Enter New Number : ")
		updated_contact[2] = new_number

	else:
		print("Invalid Input")
	update_choice_selection()
		
		
def update_contact():
	current_contact, result, updated_contact = search_contact()
	current_contact  += "\n"
	update_choice_selection()

	new_contact = "{},{},{}\n".format(updated_contact[0],updated_contact[1],updated_contact[2])

	current_index = result.index(current_contact)
	print("Before Change")
	print(result)

	result[current_index] = new_contact	
	print("After Change")
	print(result)

	write_data(result)
	print("Contact Updated Succesfully")						




def delete_contact():
	current_contact, result, updated_contact = search_contact()
	current_contact  += "\n"

	result.remove(current_contact)
	write_data(result)















