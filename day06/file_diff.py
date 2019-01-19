#!/usr/bin/env python3

with open('/tmp/passwd') as f1:
    aset = set(f1)

with open('/tmp/mima') as f2:
    bset = set(f2)

with open('/tmp/diff.txt', 'w') as f3:
    f3.writelines(bset - aset)
