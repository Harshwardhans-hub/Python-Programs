class Employee:
	def __init__(self):
		self.Employee_ID = input("Enter id : ")
		self.Name = input("Enter  Name : ")
		self.Email = input("Enter Email : ")
		self.Contact = int(input("Enter Contact"))

	def show(self):
		print("Id ",self.Employee_ID)
		print("Name : ",self.Name)
		print("Email : ",self.Email)
		print("Contact : ",self.Contact)

class Manager(Employee):
	def __init__(self):
		super().__init__()
		self.department = input("Enter Department : ")

	def mshow(self):
		super().show()
		print("Department : ",self.department)


e1 = Employee()
print("============================")
e1.show()
print("============================")

m1 = Manager()
print("============================")
m1.show()
print("============================")
m1.mshow()
print("============================")

