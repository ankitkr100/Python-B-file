#def add_tags(tag, word):
#    return "<%s>%s</%s>" % (tag, word, tag)
#print(add_tags('i', 'Python'))
#print(add_tags('b', 'Python Tutorial'))

##	return str[:2] + word + str2[2:]
#
#
#print(insert_sting_middle('[[]]', 'Python'))
#print(insert_sting_middle('{{}}', 'PHP'))
#print(insert_sting_middle('<<>>', 'HTML'))


#def insert_end(str):
#	sub_str = str[-2:]
#	return sub_str * 4
#print(insert_end('Python'))
#print(insert_end('Exercises')) 

#def first_three(str):
#	if len(str) < 3:
#		return str  
#	else:
#		sub_str = str[:3]
#		return sub_str
#print(first_three('ipy'))
#print(first_three('python'))
#print(first_three('py'))

#str1 = 'https://www.w3resource.com/python-exercises/string'
#print(str1.rsplit('/', 1)[0])
#print(str1.rsplit('-', 1)[0])

def reverse_str(str):
	if len(str) % 4 == 0:
		return ''.join(reversed(str))
	return str
print(reverse_str('nkit'))
