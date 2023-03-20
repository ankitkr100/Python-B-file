#base = 3
#exponent = 4

#result = 1

#for exponent in range(exponent, 0, -1):
#	result *= base 

#print("Answer = " + str(result)


def pow(a, b):
	if b==1:
		return a 
	else:
		return a*pow(a, b-1)

print(pow(8,2))