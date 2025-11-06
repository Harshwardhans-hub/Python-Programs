from phonebook1 import *

def recursive_menu():

	print("1.Create Contact")
	print("2.Display Contacts")
	print("3.Search Contact")
	print("4.Update Contact")
	print("5.Delete Contact")
	print("6.Exit")

	choice = int(input("Enter the choice :"))

	if choice == 1:
		create_contact()
	elif choice == 2:
		display_all_contact()
	elif choice == 3:
		search_contact()
	elif choice == 4:
		update_contact()
	elif choice == 5:
		delete_contact()
	elif choice == 6:
		return
	else:
		print("Invalid choice")
	recursive_menu()

recursive_menu()