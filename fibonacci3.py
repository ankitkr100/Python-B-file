num1 = 0
num2 = 1
print("Fibonacci sequence:")
for i in range(1, 11):
	print(num1, end=" ")
	#add last two numbers to get next number
	res = num1 + num2
	num1 = num2
	num2 = res