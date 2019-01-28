import os

print('hello world!')
ret_val = os.fork()
if ret_val:
    print('parent!')
else:
    print('child')

print('both')
