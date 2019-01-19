x = y = 10
a, b = 10, 20
print(x, ':', id(x), ', ', y, ':', id(y), ', ', a, ', ', b, sep='')
a, b = b, a
print(a, b)
