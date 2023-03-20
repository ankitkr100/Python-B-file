def check_palindrome(string):
	left_string = 0
	right_string = len(string)-1
	
	while right_string >= left_string:
	    if not string[left_string] == string[right_string]:
	         return False
	    left_string += 1
	    right_string -= 1
	return True

print(check_palindrome('abc'))