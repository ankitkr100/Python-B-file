test_str ='geeksforgeeks 33 is best'
print("The original string is : " + str(test_str))
res = sum(not chr.isspace() for chr in test_str)
print("The charecters Frequency avoiding spaces : " + str(res))