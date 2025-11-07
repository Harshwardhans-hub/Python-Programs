#import time
#import time as t

#Code to calculate the time required in execution of iterative method of factorial program.

'''from time import time

n = int(input("Enter the number : "))
start = time()
fact = 1
for i in range(1,n+1):
	fact = fact*i
print("factorial of {} is : {}".format(n,fact))
end = time()

total = end - start
print("Start Time : ",start)
print("End Time : ",end)
print("Total Time : ",total)'''

#Code to calculate the time required in execution of Recursive method of factorial program.
from time import time
start = time()
def fact(x):

	if x ==0 or x == 1:
		return 1
	else:
		return x*fact(x-1)

n = int(input("Enter the Number : "))
fact_n = fact(n)
print("Factorial of {} is : {}".format(n,fact_n))
end = time()
total = end - start
print("Start time : ",start)
print("End time : ",end)
print("Total time : ",total)


