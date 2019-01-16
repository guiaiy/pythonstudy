

print('+%s+'%('*'*48))
print('+','hello world'.center(48),'+',sep='')
print('+%s+'%('*'*48))

py_str='hao123'
print(py_str.center(50))
print(py_str.isdigit())
print(py_str.center(50,'*'))
print(py_str.ljust(50,'*'))
print(py_str.rjust(50,'*'))

print(py_str.upper())
print(py_str.lower())
print(py_str.islower())
print(py_str.isupper())

print(py_str.startswith('hao'))
print(py_str.endswith('ha'))
print(py_str.split('o'))