def exponent(base, exp):
	num = exp
	result = 1
	while num > 0:
		result = result * base
		num = num - 1
	print(base, "raise to the power of", exp, "is: ", result)
exponent(5, 4)