str1 = 'James'
print("Original string is", str1)

# Get first charecter
res = str1[0]

# Get string size
l = len(str1)

# get middle index number 
mi = int(l / 2)

res = res + str1[mi]

# Get last charecter and add it to result 
res = res + str1[l-1] 

print("New String:", res)