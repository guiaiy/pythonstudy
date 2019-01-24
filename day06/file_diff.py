#!/usr/bin/env python3

with open('/tmp/passwd') as f1:
    aset = set(f1)

with open('/tmp/mima') as f2:
    bset = set(f2)

with open('/tmp/diff.txt', 'w') as f3:
    f3.writelines(bset - aset)
    f3.writelines(aset - bset)

with open('/tmp/diff.txt') as f4:
    content = f4.read()
    print(content)
