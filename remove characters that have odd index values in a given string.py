def odd_string(str):
	result = ""
	for i in range(len(str)):
		if i % 2 == 0:
			result = result + str[i]
	return result
print(odd_string("Python"))
print(odd_string("Fish"))

