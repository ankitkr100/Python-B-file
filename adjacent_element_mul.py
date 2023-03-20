test_tup = (1, 5, 7, 8, 10)
print("The original tuple : " + str(test_tup))
res = tuple(map(lambda i, j : i * j, test_tup[1:], test_tup[:-1]))
print("resultant tuple after multiplication : " + str(res))