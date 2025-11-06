#using third variable
'''var_x = int(input("Enter x : "))
var_y = int(input("Enter_y : "))
print("x = ",var_x)
print("y = ",var_y)
temp = var_x
var_x = var_y
var_y = temp
print("x = ",var_x)
print("y = ",var_y)'''

#without using third variable
'''a = int(input("Enter a : "))
b = int(input("Enter b : "))
print("a:",a)
print("b:",b)
a=a+b
b=a-b
a=a-b
print("a:",a)
print("b:",b)'''

#only for python
a = int(input("Enter a : "))
b = int(input("Enter b : "))
a,b = b,a
print("a,b:",a,b)