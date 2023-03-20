d = {'a': 97, 'b': 98, 'c': 99, 'd': 100}
# space key added using setdefault() method

x = d.setdefault(' ', 32)
print(x)
print(d)