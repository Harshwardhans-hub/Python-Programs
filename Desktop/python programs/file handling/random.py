name = input("Enter the name : ")
email = input("Enter the email : ")
contact = input("Enter the contact : ")

file1 = open("sample1.txt","a")
file1.write(name+"\n")
file1.write(email+"\n")
file1.write(contact+"\n")
file1.close()