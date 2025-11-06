class Contact:
	def __init__ (self):
		self.name = input("Enter Name : ")
		self.contact = input("Enter the Contact number : ")
		self.email = input("Enter the Email : ")

	def display_contact(self):
		print("Name : ",self.name)
		print("Email : ",self.contact)
		print("Phone_Number : ",self.email)

	def update_contact(self):
		choice = input("Enter 1 for Name\nEnter 2 for Contact\nEnter 3 for Email\nEnter a choice : ")
		if choice == "1":
			self.name = input("Enter New Name : ")
		elif choice == "2":
			self.contact = input("Enter the New Contact number : ")
		else :
			self.email = input("Enter the New Email : ")
		print("Contact updated sucessfully")


	def delete_contact(self):
		del(self)

c1 = Contact()
c1.display_contact()


c1.update_contact()
c1.display_contact()