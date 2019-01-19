#!/usr/bin/env python3
import sys
from random import randint

import mydemo
from mydemo import foo

print(randint(1, 100))
foo.hi()
print(sys.path)
mydemo.star()
