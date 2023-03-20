test_list = [5, 6, 7]
print("The original list is: " + str(test_list))
test_tup = (9, 10)
res = tuple(list(test_tup) + test_list)
print("The container after addition: " + str(res))