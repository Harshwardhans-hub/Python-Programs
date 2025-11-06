Dict_x = {"Name":"Harsh",1:"Sunny",2.5:"Aman"}
'''print(Dict_x)
print(type(Dict_x))
'''
for i in Dict_x:
	print(i)
	print(Dict_x[i])

for j in Dict_x.values():
	print(j)

for m,n in Dict_x.items():
	print(m)
	print(n)

Dict_x["Day"]="Friday"

Dict_x["Name"] = "Harshwardhan"

Dict_x.pop(2.5)
for m,n in Dict_x.items():
	print(m)
	print(n)

