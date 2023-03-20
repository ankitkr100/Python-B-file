test_list = [12, 67, 98, 34]
# printing original list
print("The original list is : " + str(test_list))
# Sum of number digits in list
# using loop + str()
res = []
for ele in test_list:
	sum = 0
	for digit in str(ele):
		sum += int(digit)
	res.append(sum)

# printing result
print("List integer summation : " + str(res))
