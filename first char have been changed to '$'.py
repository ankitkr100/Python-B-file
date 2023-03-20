#def change_char(str1):
#	char = str1[0]
#	str1 = str1.replace(char, '$')
#	str1 = char + str1[1:]
#
#	return str1
#
#print(change_char('restart'))
#def chars_mix_up(a, b):
#	new_a = b[:2] + a[2:]
#	new_b = a[:2] + b[2:]
#
#	return new_a + ' ' + new_b
#print(chars_mix_up('abc', 'xyz'))

#def add_string(str1):
#	length = len(str1)
#	if length > 2:
#		if str1[-3:] == 'ing':
#			str1 += 'ly'
#		else:
#			str1 += 'ing'
#	return str1
#print(add_string('ab'))
#print(add_string('abc'))
#print(add_string('string'))


def not_poor(str1):
	snot = str1.find('not')
	spoor = str1.find('not')

	if spoor > snot and snot>0 and spoor>0:
		str1 = str1.replace(str1[snot:(spoor+4)], 'good')
		return str1
	else:
		return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyric is poor'))

