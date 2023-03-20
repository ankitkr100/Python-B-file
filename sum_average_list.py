#lst = [4, 5, 1, 2, 9, 7, 10, 8]
#count = sum(lst)
#print("The sum is: ", count)
#avg = count/len(lst)
#print("average = ", avg)
L = [4, 5, 1, 2, 9, 7, 10, 8]
count = 0
# Finding the sum
for i in L:
	count += i
avg = count/len(L)
print("sum = ", count)
print("average = ", avg)
