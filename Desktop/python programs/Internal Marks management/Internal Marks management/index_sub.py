from subjects import *
def sub_menu():
    
        print("\n1. Add Subject")
        print("2. View Subjects")
        print("3. Update Subject")
        print("4. Delete Subject")
        print("5. Exit")
        choice = int(input("Enter the choice : "))

        if choice == 1:
            add_subjects()
        elif choice == 2:
            view_subjects()
        elif choice == 3:
            update_subject()
        elif choice == 4:
            delete_subject()
        elif choice == 5:
            return 
        else:
            print("Invalid choice")

sub_menu()
