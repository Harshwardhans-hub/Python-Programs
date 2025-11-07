# Electricity bill calculations
n = int(input("Enter the units of electricity consumed : "))
cost = 0
if 0<n<100:
	cost = 5                       # cost in rupees
	print("The amount of electricity bill : {}".format(n*cost))
elif 101<n<200: 
	cost = 7
	print("The amount of electricity bill : {}".format(n*cost))	
elif 201<n<300:
	cost = 9
	print("The amount of electricity bill : {}".format(n*cost))	
else: 
	cost = 10
	print("The amount of electricity bill : {}".format(n*cost))	