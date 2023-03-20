str1 = "PyNative"
lower=[]
upper=[]
for ch in str1:
	if ch.islower():
		lower.append(ch)
    else:
	    upper.append(ch)

#join both the list
sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)