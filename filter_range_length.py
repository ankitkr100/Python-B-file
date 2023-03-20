test_list = [(4,), (5,6), (2,3,5), (5,6,8,2), (5,9)]
print("the original list is : " + str(test_list))
i, j = 2, 3
res = [sub for sub in test_list if len(sub) >= i and len(sub) <= j]
print("The tuple list after filtering range records: " + str(res))