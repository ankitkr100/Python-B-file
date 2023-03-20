def check_prime(num):
	for i in range(2, num-1):
		if (num % i==0):
		     return print("The number is not Prime")
		else:
			 return ("The number is Prime")
	    	 
num = 17
print(check_prime(num))


