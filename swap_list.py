test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
# printing original lists
print("Teh original list is : " + str(test_list))
res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]
print("List after performing character swaps : " + str(res)")