#!/usr/bin/env python3

stopword = ''
str = ''
for line in iter(input, stopword):
    str += line + '\n'

print(str)
