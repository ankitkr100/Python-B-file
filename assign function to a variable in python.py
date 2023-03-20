#1)
#def a():
#	print("GFG")
# Assigning function to a variable 
#var=a 
# calling the variable
#var()

#2)
#defined function
#x = 123
#def sum():
#	x = 98
#	print(x)
#	print(globals()['x'])
# Driver code
#print(x)
#z = sum
# Invoke function
#z()
#z()

#3
#global variable
#a = 5
#def func():
#	c = 10
#	d = c + a
	#calling globals()
#	globals()['a'] = d
#	print(d)
# Driver code
#func()

# global variable
#name = 'gautam'
#print('Before modification:', name)
#Calling global function
#globals()['name'] = 'gautam karakoti'
#print('After modification:', name)

#	print("Inside the method B.")
#def A():
#	print("Inside the method A.")
#
#	return B
#
#returned_function = A()
#returned_function()

#def B(st2):
#	print("Good" + st2 + ".")
# First method that return second method
#   print(st1 + " and ", end = "")
#
 #   # return second method
 #   return B(st2)
#A("Hello", "Morning")
#B("Good")

#def A(u, v):
#	x = u + v 
#	z = u - v 
#	return lambda: print(x*z)
#
#returned_func = A(25, 20)
#print(returned_func)
#returned_func()

#def calculate_sum(a, b):
#	return a + b

#x=2
#y=5
#print(calculate_sum(x,y))

#def=12
#if=2
#print(calculate_sum(def, if))

#var1 = 46
#var2 = 23
#print(var1 * var2)

#var@ = 12
#$var = 55
#print(var@ * $var)

#def my_function():
#	print('This is a fuction with invalid identifier')
#my_function()

#var1 = 23
#ABC = "This is a string"
#fr12 = 20
#x_y = 'GFG'
#slp__72 = 'QWERTY'
#print(var1 * fr12)
#print(ABC + slp__72)

#def sum(a, b):
#	print("The data type of a is:", type(a))
#	print("The data type of b is:", type(b))
#	return a+b
#
#print(sum(5, 4))
#print(sum(float(23), float(27)))

#def concatenate(a, b):
#	print("The type of a is:", type(a))
#	print("The type of b is:", type(b))
#	return a+b

#x = 120.0
#y= 789
#print(concatenate(x, y))
#print(concatenate(str(x), str(y)))

#def no_of_argu(*args):
#	return len(args)
#a=4
#b=5
#n = no_of_argu(1, 2, 3, a)
#print("The number of argument is:", n)

#def no_of_argu(*args):
#	return len(args)


print(no_of_argu(1, 2, 3))
print(no_of_argu(1, 2, 3, 4, 5))
print(no_of_argu(1, 2))
print(no_of_argu(1, 2, 3, 5, 6, 5, 4))
print(no_of_argu(1))












