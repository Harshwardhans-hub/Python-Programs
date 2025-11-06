from marks_management import *

def menu():

    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Add Internal Marks")         
    print("6. View Internal Marks")   
    print("7. Modify Internal Marks")  
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":                     
        subject = input("Enter subject:")
        add_internaL_marks(subject)
    elif choice == "6":                     
        subject = input("Enter subject : ")
        view_internal_marks(subject)
    elif choice == "7":
        subject = input("Enter subject : ")
        modify_internal_marks(subject)
    elif choice == "8":
        return
    else:
        print("Invalid Choice.")
    menu()

menu()
