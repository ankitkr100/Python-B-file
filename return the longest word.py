def find_longest_word(word_list):
	word_len = []
	for n in word_list:
		word_len.append((len(n), n))
	word_len.sort()
	return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "Excercise", "Backend"])
print("\nLongest word: ", result[1])
print("Length of the longest word:", result[0])