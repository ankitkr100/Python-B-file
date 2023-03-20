def merge_list(list1, list2):
    result_list = []
    for num in list1:
	    if num % 2 != 0:
	       result_list.append(num)
	# iterate second list
    for num in list2:
	    if num % 2 == 0:
	  	   result_list.append(num)
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))