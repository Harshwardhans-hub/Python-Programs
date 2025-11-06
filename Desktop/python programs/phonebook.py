def create_contact(x):
	contact_name = input("Enter Name : ")
	contact_number = int(input("Enter Number : "))
	contact_email = input("Enter Email : ") 
	contact_entry = {"name": contact_name, "contact": contact_number, "email": contact_email}
	Master_data_list.append(contact_entry)
	print("Contact created successfully : ",Master_data_list)
#for all contacts
def Display_contact():
	print("+++++++++++++++++++++++")
	for i in Master_data_list :
		print("Name : ",i["name"])
		print("Contact : ",i["contact"])
		print("Email : ",i["email"])
		print("+++++++++++++++++++++++")
#for single contact
def display(i):
	print("+++++++++++++++++++++++")
	print("Name : ",i["name"])
	print("Contact : ",i["contact"])
	print("Email : ",i["email"])
	print("+++++++++++++++++++++++")


def Search_contact():
	search_contact = input("Enter the search term :")
	for i in Master_data_list : 
		for m in i.values(): 
			if search_contact == m :
				return i 
	else : 
		return None 
	

def Update_contact():
	x = Search_contact()
	y = x 
	display(x)
	choice = input("Enter 1 to Change the name\nEnter 2 to change contact\nEnter 3 to change email\nEnter Choice :")
	value = input("Enter Values")
	if choice == "1" : 
		x["name"]  = value
	elif choice == "2":
		x["contact"] = value
	elif choice == "3":
		x["email"] = value
	else :
		print("Invalid Choice")

	for i in Master_data_list : 
		if i == y : 
			z = Master_data_list.index(i)
			Master_data_list[z] = x


	Display_contact()

def Delete_contact(x):
	global Master_data_list
	choice = int(input("Enter 1 to delete a particular person's contact details.\nEnter 2 to delete full phone book.\nEnter choice: "))	
	
	if choice == 1:
		x = Search_contact()
		display(x)
		if x in Master_data_list:
			Master_data_list.remove(x)
			print("Contact deleted successfully.")
			print("Updated contacts list : ",Master_data_list)
		else: 
			print("Contact not found.")

	elif choice == 2:
		del Master_data_list
		Master_data_list = []
		print("Phone book deleted successfully.")
		print("Updated phone contacts",Master_data_list)

	else:
		print("Invalid Choice.")

Dict_details = {}
Master_data_list = [
	{"name": "Rohit", "contact": 7566565443, "email": "qwe@gmail.com"},
	{"name": "Bohit", "contact": 9766565443, "email": "ytt@gmail.com"},
	{"name": "mohit", "contact": 666565443, "email": "qwerty@gmail.com"}
]


while True:
	print("1. Create Contact")
	print("2. Display Contacts")
	print("3. Search Contact")
	print("4. Update Contact")
	print("5. Delete Contact")
	print("6. Exit")

	choice = int(input("Enter your choice : "))
	if choice == 1:
		create_contact(Dict_details)
	elif choice == 2:
		Display_contact()
	elif choice == 3:
		contact = Search_contact()
		if contact == None :
			print("Contact not found ")
		else : 
			display(contact)
	elif choice == 4:
		Update_contact()
	elif choice == 5:
		Delete_contact(Dict_details)
	elif choice == 6:
		break
	else:
		print("Invalid choice.")
	
