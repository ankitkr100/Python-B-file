str1 = "Emma-is-a-data-scientist"
print("Original string is:", str1)

# split string 
sub_strings = str1.split("_")

print("Displaying each substring")
for sub in sub_strings:
	print(sub)