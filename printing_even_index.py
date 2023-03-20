word = input('Enter word')
print("Original string:", word)
#get the length of the string
size = len(word)
print("Printing only even index chars")
for i in range(0, size - 1, 2):
	print("index[", i, "]", word[i])