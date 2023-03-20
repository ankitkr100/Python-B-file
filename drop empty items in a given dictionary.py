dict = {'c1': 'Red', 'c2':'Green', 'c3':None}
print("Original dictionary")
print(dict)
dict = {key: value for (key, value) in dict.items() if value is not None}
#dict.pop('c3')
print(dict)