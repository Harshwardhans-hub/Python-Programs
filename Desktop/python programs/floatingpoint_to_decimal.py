def float_to_binary_converter(num):
	output = ""

	x = int(num)
	y = num - x
	result_x = convert_x(x)
	result_y = convert_y(y)
	return result_x+"."+result_y


def convert_x(x):
	a = ""
	while(x>0):
		remainder = x % 2
		a = a + str(remainder)
		x = x // 2
		return a[::-1]
	
	

def convert_y(y):
	b=""
	while(y == 0 ):
			y = y*2 
			b = b + str(y)
		return b
	

num = float(input("Enter the value: "))
convert_value = float_to_binary_converter(num)
print("Binary Conversion of {} = {}".format(num,convert_value))
	







