def exchange(str):
	return str[-1:] + str[1:-1] + str[:1]
print(exchange('abcd'))
print(exchange('12345'))