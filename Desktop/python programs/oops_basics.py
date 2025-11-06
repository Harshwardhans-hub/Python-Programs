class Student:
	def __init__ (self):
		self.name = input("Enter Name : ")
		self.address = input("Enter Address : ")
		self.email = input("Enter Email : ")

	def show(self):
		print("Name : ",self.name)
		print("Adress : ",self.address)
		print("Email : ",self.email)

s1 = Student()	
s1.show()