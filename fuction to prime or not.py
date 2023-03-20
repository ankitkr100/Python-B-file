def check(num):
	for i in range(2, num):
		if num % i == 0:
		   return False
		else:
			return print("The number is prime")
num = 29
print(check(num))