class person:
	def __init__(self, first, last):
		self.firstn = first
		self.lastn = last
	def Name(self):
		return self.firstn + " " + self.lastn
class Emp(person):
	def __init__(self, first, last, staffnum):
		person.__init__(self, first, last)
		self.staffno = staffnum
	def GetEmp(self):
		return self.Name() + ", " + self.staffno

a = person("Alex", "Karlos")
b = Emp("Alex", "Karlos", "A102")

print(a.Name())
print(b.GetEmp())