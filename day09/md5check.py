#!/usr/bin/env python3
import hashlib
from sys import argv


def check_md5(fname):
    alldata = hashlib.md5()
    with open(fname, 'rb') as f1:
        while True:
            data = f1.read(4096)
            if not data:
                break
            alldata.update(data)
    return alldata.hexdigest()


if __name__ == '__main__':
    for i in argv[1:]:
        print(check_md5(i))
