from collections import Counter
test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]
print("The original list is : " + str(test_list))
res = [(*key, val) for key, val in counter(test_list).items()]
print("frequency Tuple list: " + str(res))