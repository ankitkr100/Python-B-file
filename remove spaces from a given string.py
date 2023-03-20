#def remove_spaces(str1):
#	str1 = str1.replace(' ','') 
#	return str1
#
#print(remove_spaces("w 3 res ou r ce"))
#print(remove_spaces("a b c"))

#def move_Spaces_front(str1):
#	noSpaces_char = [ch for ch in str1 if ch!=' ']
#	spaces_char = len(str1) - len(noSpaces_char)
#	result = ' '*spaces_char 
#	result = '"'+result + ''.join(noSpaces_char)+'"'
#	return(result)
#
#print(move_Spaces_front("w3resource . com "))
#print(move_Spaces_front("   w3resource.com  "))

#def get_max_occuring_char(str1):
#	ASCII_SIZE = 256
#	ctr = [0] * ASCII_SIZE
###	for i in str1:
#
#	for i in str1:a
#		if max < ctr[ord(i)]:
#			max = ctr[ord(i)]
#			ch = in
#		return ch 
#print(get_max_occuring_char("Python: Get file creation and notification"))
#print(get_max_occuring_char("abcdefghijkb"))

def capitalize(str):
	str = new_str = str.title()
	new_str = ""
	for word in str.split():
	    new_str += word[:-1] + word[-1:].upper() + " "
	return new_str[:-1]

print(capitalize("ankit is a good boy"))
#print(new_str)

















