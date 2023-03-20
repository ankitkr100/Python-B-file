def filter_even(dictt):
	result = {key: [idx for idx in val if not idx % 2]
	      for key, val in dictt.items()}
	return result

students = {'V' : [1, 4, 6, 10], 'VI' : [1, 4, 12], 'VII' : [1, 3, 8]} 
print("Original Dictionary:")
print(students)
print("Filter even numbers from said dictionary:")
print(filter_even(students))