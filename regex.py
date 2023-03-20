import re
str = "Example for meta charecters in Regular expression"
str2 = "123 A friend in need is a friend is deed" 
res = re.findall("[^abc]",str)
print(res)

#import re
#str = "Ankit Kumar"
#x = re.search("Ankit Kumar",str)
#print(x)

#import re 
#str = "Example for 123 Meta Chatrecters in Regular Expression"
#res = re.findall("[0-9][0-9][0-9]",str)
#print(res)
#import re
#def is_allowed_specific_char(string):
#	charRe = re.compile(r'[^a-zA-Z0-9]')
#	string = charRe.search(string)
#	return not bool(string)
#print(is_allowed_specific_char("ABCDEFabcdef123450")) 
#print(is_allowed_specific_char("*&%@#!}{"))




