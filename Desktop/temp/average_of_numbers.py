#a python script to find average of n user defined integers
n = int(input("Enter the number of integers : "))

sum = 0
for i in range(n):
	num = int(input("Enter the integer : "))
	sum += num

average = sum/n
print("The average of {} numbers is : {} ".format(n,average)) 
