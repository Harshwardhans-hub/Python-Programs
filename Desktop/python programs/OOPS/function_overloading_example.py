'''def area(x):    #Will perform function overriding instead of overloading  
	return (22/7)*x*x

def area(x,y):
	return x*y

a1 = area(5)
print(a1)

a2 = area(8,6)
print(a2)'''

def area(x,y=None):
	if y == None:
		return (22/7)*x*x
	else:
		return x*y

a1 = area(5)
print(a1)
a2 = area(8,6)
print(a2)