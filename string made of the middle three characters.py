str = "JohnDipPeta"
print("The original string is:", str)

l = len(str)
mi = int(l/2)
res = str[mi-1] + str[mi] + str[mi+1]
print("The new string is:", res)