def make_map(S):
	temp_map = {}
	for char in s:
		if char not in temp_map:
			temp_map[char] = 1
		else:
			temp_map[char] += 1
	return temp_map
def make_anagram(str1, str2):
	str1_map1 = make_map(str1)
	str2_map2 = make_map(str2)

	ctr = 0
	for key in str2_map2.keys():
		if key not in str1_map1:
			ctr += str2_map2[key]
		else:
			ctr += max(0, str2_map2[key]-str1_map1[key])
	return ctr
str1 = input("Input string1: ")
str2 = input("Input string2: ")
print(make_anagram(str1, str2))