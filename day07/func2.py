#!/usr/bin/env python3
from functools import partial


def add(a, b, c, d):
    print(a+b+c+d)


myadd = partial(add, 10, 20, 30)

myadd(40)