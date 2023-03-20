def remove_charecter(str1, c):
	return ' '.join([ch for ch in str1 if ch == c])

text = "Python excercises"
print("Original string")
print(text)
except_char = "P"
print("Remove all charecters except", except_char,"in the said string:")
print(remove_charecter(text, except_char))