#x = 3
#y = 123
#print("\nOriginal Number:", x)
#print("Formatted Number(left padding, width 2): "+"{:0>2d}".format(x));
#print("Original Number:", y)
#print("Formatted Number(left padding, width 6): "+"{:0>6d}".format(y));
#print()

x = 3
y = 123
print("\nOriginal Number", x)
print("Formatted Number(right padding, width 2): "+"{:*< 3d}".format(x));
print("Original Number:", y)
print("Formatted Number(right padding, width 6): "+"{:*< 7d}".format(y));
print()



