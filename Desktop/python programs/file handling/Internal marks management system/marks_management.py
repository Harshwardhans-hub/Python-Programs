#Student details 
def add_student():
	name = input("Enter Name : ")
	roll_no = input("Enter Roll_no : ")
	course = input("Enter course : ")
	student_entry = "{},{},{}\n".format(name,roll_no,course)
	file = open("studentdetails.txt","a")
	file.write(student_entry)
	file.close()
	print("Student Added Successfully.")

def view_students():
    file = open("studentdetails.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.replace("\n", "")
        student = line.split(",")
        print("++++++++++++++++++++++++")
        print("Name      :", student[0])
        print("Roll No   :", student[1])
        print("Course    :", student[2])
        print("++++++++++++++++++++++++")


def update_student():
    roll_no = input("Enter the Roll_No of student whose details are to be updated: ")
    file = open("studentdetails.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("studentdetails.txt", "w")
    updated = 0

    for line in lines:
        temp = line.split(",")
        current_roll = temp[1].replace("\n", "")

        if current_roll == roll_no:
            print("Enter the choice for updation:")
            print("1. Name\n2. Roll_No\n3. Course")
            choice = input("Enter choice : ")

            new_name = temp[0]
            new_roll = temp[1].replace("\n", "")
            new_course = temp[2].replace("\n", "")

            if choice == "1":
                new_name = input("Enter new Name: ")
            elif choice == "2":
                new_roll = input("Enter new Roll No: ")
            elif choice == "3":
                new_course = input("Enter new Course: ")
            else:
                print("Invalid choice.")
                file.write(line)
                

            file.write(new_name + "," + new_roll + "," + new_course + "\n")
            updated = 1
        else:
            file.write(line)

    file.close()

    if updated == 1:
        print("Student record updated.")
    else:
        print("Student not found.")


def delete_student():
	pass

#Internal marks storage and management

def add_internaL_marks(subject):
	
	roll_no = input("Enter roll number : ")
	mark1 = input("Enter first Internal marks : ")
	mark2 = input("Enter second Internal marks : ")
	mark3 = input("Enter third Internal marks : ")

	entry = "{},{},{},{}\n".format(roll_no,mark1,mark2,mark3)
	if subject == "dbms":
		file = open("dbms.txt","a")
	elif subject == "python":
		file = open("python.txt","a")
	else:
		print("Invalid subject.")
		return

	file.write(entry)
	file.close()
	print("Marks added to : ",subject)


def view_internal_marks(subject):
	if subject == "dbms":
		file = open("dbms.txt","r")
	elif subject == "python":
		file = open("python.txt","r")
	else:
		print("Invalid Choice")
		return

	read = file.readlines()
	file.close()

	for i in read:
		i = i.replace("\n","")
		p = i.split(",")
		print("Roll_No",p[0])
		print("Interal Marks : {},{},{}".format(p[1],p[2],p[3]))
		print("++++++++++++++++")


def modify_internal_marks(subject):
	roll_no = input("Enter the roll no to Modify marks : ")
	if subject == "dbms":
		file = open("dbms.txt","r")
	elif subject == "python":
		file = open("python.txt","r")
	else:
		print("Invalid Choice")


	read = file.readlines()
	file.close()

	modified = 0

	if subject == "dbms":
		file = open("dbms.txt","w")
	elif subject == "python":
		file = open("python.txt","w")

	for i in read:
		i = i.replace("\n","")
		temp = i.split(",")

		if temp[0] == roll_no:
			print("Present marks : {},{},{}".format(temp[1],temp[2],temp[3]))

			new_entry = "{},{},{},{}\n".format(roll_no,mark1,mark2,mark3)
			file.write(new_entry)
			print("Marks Updated Succesfullu")
		else:
			file.write(i+"\n")
		file.close()

		if modified == 0:
			print("Roll no is not found")




