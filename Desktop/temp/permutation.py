def fact(x):
	result = 1 
	for m in range(1,x+1):
		result = result * m
	return result 


n = int(input("Enter the value of n : "))
r = int(input("Enter the value of r : "))

"""fact_n = 1 
for i in range(1,n+1):
	fact_n *=i

fact_nr = 1
for j in range(1,n-r+1):
	fact_nr*=j"""

npr = fact(n) / (fact(n-r) * fact(r)) 

print("combination of {} over {} = {}".format(r,n,npr))