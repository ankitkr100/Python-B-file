#def perfect(num):
#	sum =0
#for num in range(1, 1000):
#    for i in range(1, num):
#    	if num % i == 0:
#    		sum = sum + i 
#    if sum == num:
#        return True
#    else: 
#        return false
#for i in range(1, 1001):
#    if perfect(i):
#print(perfect(num))

def perfect(n):
  sum = 0
  for i in range(1,n):
    if n%i == 0:
      sum = sum + i
  if sum == n:
    return True
  else:
    return False
for i in range(1,1001):
  if perfect(i):
    print(i)
