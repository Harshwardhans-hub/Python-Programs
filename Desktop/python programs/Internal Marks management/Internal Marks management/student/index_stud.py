from student import *
def menu():
	print("1.Add student\n2.View student\n3.Update Student\n4.Delete student")
	choice = int(input("Enter the choice : "))
	if choice == 1:
		get_student()
	elif choice == 2:
		view_student()
	elif choice == 3:
		update_student()
	elif choice == 4:
		delete_student()
	else:
		print("Invalid choice")
	menu()
menu()













