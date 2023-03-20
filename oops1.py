class Dog:
	# Class attribute
	attr1 = "mammal"
	# Instance attribute
	def __init__(self, name):
		self.name = name
	# Driver code
	# Object Instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
	#Accesing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))




