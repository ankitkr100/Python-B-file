#items=[n for n in input().split('-')]
#items.sort()
#print('-'.join(items))

# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included). Go to the editor

#def square(num):
#	for num in range(1, 31):
#		sq = num * num
#		print("The square of num is:", sq)
#num = 11
#print(square(num))

#def printValues():
#	l = list()
#	for i in range(1, 21):
#		l.append(i**2)
#	print(l)
#
#printValues()

#def abc():
#	x = 1
#	y = 2
#	str1 = "w3resource"
#	print("Python Excercise")
#
#print(abc.__code__.co_nlocals)

from time import sleep
import math
def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
print("Square root after specific milisecond:")
print(delay(lambda x: math.sqrt(X), 100, 16))
print(delay(lambda x: math.sqrt(X), 1000, 100))
print(delay(lambda x: math.sqrt(X), 2000, 25100))
