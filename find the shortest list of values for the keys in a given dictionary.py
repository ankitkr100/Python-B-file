def test(dictt):
	min_value = 1
	result = [k for k, x in dictt.items() i == (min_value)]
	return result

dictt = {
 'V': [10, 12],
 'VI': [10],
 'VII': [10, 20, 30, 40],
 'VIII': [20],
 'IX': [10,30,50,70],
 'X': [80]
 }

print("\nOriginal Dictionary:")
print(dictt)
print("\n Shortest list of values with the keys of the said dictionary:")
print(test(dictt))