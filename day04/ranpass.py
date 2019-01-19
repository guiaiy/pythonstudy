import random

box = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+'

randpass = ''
for i in range(8):
    str = random.choice(box)
    randpass += str

print(randpass)
