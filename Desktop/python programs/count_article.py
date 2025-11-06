def count_a(x) :
	global Article_Count 
	result = 0
	for i in range(len(x)):
		if i == 0 and x[i] == "a" and x[i+1] ==" " :
			result += 1
			Article_Count +=1
		elif x[i] == "a" and x[i-1] == " " and x[i+1] ==" ":
			result += 1
			Article_Count +=1
	return result

def count_an(x) : 
	global Article_Count
	result = 0
	for i in range(len(x)):
		if i == 0 and x[i] == "a"  and x[i:i+2] == "an" and x[i+2] ==" " :
			result += 1
			Article_Count +=1
		elif x[i] == "a" and x[i:i+2] == "an" and x[i-1] == " " and x[i+2] ==" ":
			result += 1
			Article_Count +=1
	return result

def count_the(x) : 
	global Article_Count
	result = 0
	for i in range(len(x)):
		if i == 0 and x[i] == "t" and x[i:i+3] == "the" and x[i+3] ==" " :
			result += 1
			Article_Count +=1
		elif x[i] == "t" and x[i-1] == " " and x[i+3] ==" " and x[i:i+3] == "the":
			result += 1
			Article_Count +=1
	return result

para = "a young girl walked into a library with an old, tattered book in her hand. She was searching for a quiet corner to read, but the noise from a nearby group distracted her. The librarian, noticing her struggle, pointed to a secluded section behind the large shelves. There, she found an empty chair and a wooden table with a small lamp. As she flipped through the pages, she discovered a hidden note between the chapters — a message from an unknown author who had visited the library years ago. The mystery intrigued her, and she decided to spend the afternoon solving the clues left behind India."
Article_Count = 0
x = count_a(para)
y = count_an(para)
z = count_the(para)

print("Paragraph = ",para)
print("Total Article Count = ",Article_Count)
print("Count of 'a' = ",x)
print("Count of 'an' = ",y)
print("Count of 'the' = ",z)