#Python script for printing only resultant values of the table 
"""x = int(input("Enter the number whose table is required : "))

for i in range(1,11):
	print(x * i)"""


"""x = int(input("Enter Value : "))
y = 0
for i in range(1,11):
	y = y + x
	print("{} * {} = {}".format(x,i,y))"""

x = int(input("Enter Value :"))
for i in range(x,x*10+1,x):
	print(i)