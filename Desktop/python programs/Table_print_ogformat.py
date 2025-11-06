#Python script for printing only resultant values of the table 
x = int(input("Enter the number whose table is required : "))

for i in range(1,11):
	print("{}*{} = {}".format(x,i,x*i))