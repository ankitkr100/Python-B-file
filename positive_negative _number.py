list1 = [10, -21, 4, -45, 66, -93, 1]
only_pos = [num for num in list1 if num >= 1]
pos_count = len(only_pos)
print("Positive numbers in the list: ", pos_count)
print("Negative number in the list: ", len(list1) - pos_count)