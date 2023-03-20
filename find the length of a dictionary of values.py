def len_values(dictt):
	count = {}
	for val in color_dict.values():
		count[val] = len(val)
	return count

color_dict = {1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}
print("\nOriginal dictionary:")
print(color_dict)
print("Length of dictionary")
print(len_values(color_dict))