#def factorial(n):
#	if n == 0:
#		return 1
#	else:
#		return n * factorial(n-1)
#n = 5#int(input("Input a number to compute the factorial:"))
#print(factorial(n))


#def test_range(n):
#	if n in range(3, 9):
#		print("%s is in the range"%str(n))
#	else:
#		print("The number is outside the given range")
#test_range(10)
#def string(s):
#	d={"UPPER_CASE":0, "LOWER_CASE":0}
#	for ch in s:
#		if ch.isupper():
#			d["UPPER_CASE"]+=1
#		elif ch.islower():
#           d["LOWER_CASE"]+=1 
#       else:
#        	pass
#   print("Original String:", s)
#    print("No. of Upper case charecters:", d["UPPER_CASE"])
#   print("No. of Lower case charecters:", d["LOWER_CASE"])
#string('The quick Brown Fox')


def unique_list(l

	):
	x = []
	for a in l:
		if a not in x:
			x.append(a)
	return x
print(unique_list([1,2,3,3,3,3,4,5]))





