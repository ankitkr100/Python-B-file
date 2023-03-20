def input(*args):
	sum = 0
	for i in args:
		sum = sum + i
	avg = sum / len(args)
	return avg

print("The average is", input(1, 2, 3))
print("The average is", input(1, 2, 3, 4, 5))
print("The average is", input(1, 2, 3, 4, 5, 6, 7))