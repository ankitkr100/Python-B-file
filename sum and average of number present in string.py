#def sum_avg():
total = 0
cnt = 0
str1 = "PYnative29@#8496"
for ch in str1:
	if ch.isdigit():
		total += int(ch)
		cnt += 1
avg = total / cnt
print("Sum is:", total, "Average is", avg)


