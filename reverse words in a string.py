def reverse_words(text):
	for line in text.split('\n'):
		return(''.join(line.split()[::-1]))
print(reverse_words("The quick brown fox jumps over the lazy dog"))
print(reverse_words("Python Excercises"))