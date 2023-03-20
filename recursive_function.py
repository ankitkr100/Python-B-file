def sum(i):
	#This is a recursive function to find sum upto i
	if (i<0 or i>10):
		return 0
	else:
		return(i + sum(i-1))
i = 10
print("The sum upto", i, "is", sum(i))