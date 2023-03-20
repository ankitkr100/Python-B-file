num = 5
factorial = 1
for i in range(1, num + 1):
	if i > 0:
	   factorial = factorial * i
	else:
	    print("Factorial doesn't exist")

print("The factorial of", num, "is", factorial)

