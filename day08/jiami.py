#!/usr/bin/env python3
import hashlib

m = hashlib.md5(b'123456')
a = m.hexdigest()
print(a)

with open('/etc/passwd', 'rb') as f1:
    data = f1.read()

a = hashlib.md5(data).hexdigest()
print(a)

m = hashlib.md5()
m.update(b'12')
m.update(b'34')
m.update(b'56')
a = m.hexdigest()
print(a)
