def to_uppercase(str):
	num_upper = 0
	for ch in str[:4]:
		if ch.upper() == ch:
			num_upper += 1
	if num_upper >= 2:
		return str.upper()
	return str

print(to_uppercase('Python'))
print(to_uppercase('PyThon'))