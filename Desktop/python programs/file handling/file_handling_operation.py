file1 = open("sample.txt","a")
file1.write("I am Harsh")
file1.write("I live in indore\n")
file1.close()


file2 = open("sample.txt","r")
x = file2.readlines()
print(x)
print(type(x))
file2.close()