def get_student():
	roll_no = input("Enter Roll.No : ")
	name = input("Enter Name : ")

	student_entry = "{},{}\n".format(roll_no,name)
	file = open("student.txt","a")	
	file.write(student_entry)
	file.close()
	print("Student added successfully")

def view_student():
	file = open("student.txt","r")
	read = file.readlines()
	file.close()
	print("Student details fetched successfully.")
	for i in read:
		i = i.replace("\n","")
		detail = i.split(",")
		
		print("+++++++++++++")
		print("Roll.no : ",detail[0])
		print("Name : ",detail[1])
		print("++++++++++++++")

def update_student():
	roll_no = input("Enter Roll.No : ")
	file = open("student.txt", "r")
	read = file.readlines()
	file.close()

	file = open("student.txt", "w")
	updated = 0

	for i in read:
		temp = i.split(",")
		current_roll = temp[0].replace("\n", "")  	 

		if current_roll == roll_no:
			print("Enter the choice :") 
			print("1.Name\n2.Roll no\n")
			choice = input("Choice: ")

			new_name = temp[1].replace("\n", "")
			new_roll = temp[0]

			if choice == "1":
				new_name = input("Enter new Name : ")
			elif choice == "2":
				new_roll = input("Enter new Roll_no : ")		
			else:
				print("Invalid choice")
				file.write(i)
				continue

			file.write(new_roll + "," + new_name + "\n") 
			updated = 1
		else:
			file.write(i)

	file.close()

	if updated == 1:
		print("Record updated successfully")
	else:
		print("Record not found")

def delete_student():
	roll_no = input("Enter Roll.No to delete: ")
	file = open("student.txt", "r")
	read = file.readlines()
	file.close()

	file = open("student.txt", "w")
	deleted = 0

	for i in read:
		temp = i.split(",")
		current_roll = temp[0].replace("\n", "")

		if current_roll == roll_no:
			deleted = 1
		else:
			file.write(i)

	file.close()

	if deleted == 1:
		print("Record deleted successfully")
	else:
		print("Record not found")

