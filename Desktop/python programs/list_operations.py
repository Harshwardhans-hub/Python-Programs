list_x = [2,4.50,"a",2+6j,2]
print(list_x)
print(type(list_x))

#reading the element from the list using index
for i in range(len(list_x)):
	print(list_x[i])
	print(type(list_x[i]))

#iteratable
	for i in list_x:
		print(i)
		print(type(i))

#updation 

list_x.append("Indore")                 #adding element at last
print(list_x)

list_x.insert(2,"m.p")                  #adding element in between 
print(list_x)

#replacing
y = list_x.index(2)
list_x[y] = "mango"
print(list_x)