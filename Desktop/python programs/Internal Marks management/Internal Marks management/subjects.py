def add_subjects():
	sub_name = input("Enter subject Name : ")
	sub_code = input("Enter subject Code : ")
	sub_details = {"sub_name": sub_name, "sub_code": sub_code}

	file = open("subjects.txt", "a")
	file.write(str(sub_details) + "\n")
	file.close()
	print("Subject added successfully.")

def view_subjects():
	file = open("subjects.txt","r")
	read = file.readlines()
	file.close()

	if len(read) == 0:
		print("No subjects found")
		return
	print ("\n List of Subjects :")
	for i in read:
		print(i,end="")


def update_subject():
	sub_code = input("Enter the subject code to update : ")
	file = open("subjects.txt","r")
	read = file.readlines()
	file.close()

	file = open("subjects.txt","w")
	updated = 0
	
	for i in read:
		if sub_code in i:
			new_name = input("Enter the new name of subject : ")
			new_code = input("Enter the new code of subject : ")
			subject_entry = "{{'sub_name':'{}','sub_code':'{}'}}\n".format(new_name,new_code)
			file.write(subject_entry)
			updated = 1 
		else:
			file.write(i)
	file.close()

	if updated == 1:
		print("Subject updated successfully")
	else:
		print("Subject not found")

def delete_subject():
	sub_code = input("Enter the subject code to delete : ")
	file = open("subjects.txt", "r")
	read = file.readlines()
	file.close()

	file = open("subjects.txt", "w")
	deleted = 0

	for i in read:
		if sub_code in i:
			deleted = 1
		else:
			file.write(i)
	file.close()
	if deleted == 1:
		print("Subject deleted successfully")
	else:
		print("Subject code not found")
