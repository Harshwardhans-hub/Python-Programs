from Internal_mark import *

def marks_menu():
    while True:
        print("Select subject:")
        print("1. English")
        print("2. Hindi")
        print("3. Maths")
        print("4. Exit")
        subj_choice = int(input("Enter choice: "))

        if subj_choice == 1:
            subject = "english"
        elif subj_choice == 2:
            subject = "hindi"
        elif subj_choice == 3:
            subject = "maths"
        elif subj_choice == 4:
            break
        else:
            print("Invalid choice")
            continue

        while True:
            print("\nSelect internal:")
            print("1. Internal 1")
            print("2. Internal 2")
            print("3. Internal 3")
            print("4. Back to subject selection")
            internal_choice = int(input("Enter choice: "))

            if internal_choice == 1:
                internal_file = "Internal_first_{}.txt".format(subject)
            elif internal_choice == 2:
                internal_file = "Internal_second_{}.txt".format(subject)
            elif internal_choice == 3:
                internal_file = "Internal_third_{}.txt".format(subject)
            elif internal_choice == 4:
                break

            else:
                print("Invalid internal choice")
                continue

            while True:
                print("Operations:")
                print("1. Add marks")
                print("2. View marks")
                print("3. Update marks")
                print("4. Delete marks")
                print("5. Back to internal selection")
                choice = int(input("Enter operation choice: "))

             
                if choice == 1  :
                    add_marks(internal_file)
                elif choice == 2:
                    view_marks(internal_file)
                elif choice == 3:
                    update_marks(internal_file)
                elif choice == 4:
                    delete_marks(internal_file)
                elif choice == 5:
                    break
                else:
                    print("Invalid choice")

marks_menu()
