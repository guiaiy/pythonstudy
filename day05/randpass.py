#!/usr/bin/env python3
import string
import random

def getranpass(long=6):
    str = string.ascii_letters+string.digits
    result = ''
    for i in range(long):
        letter = random.choice(str)
        result = result + letter
    return result

if __name__ == '__main__':
    password=getranpass(8)
    print(password)