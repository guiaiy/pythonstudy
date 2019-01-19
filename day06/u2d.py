#!/usr/bin/env python3
import sys


def unix2dos(fname):
    dest_fname = fname + '.txt'
    with open(fname) as src:
        with open(dest_fname, 'w') as dest:
            for content in src:
                line = content.rstrip() + '\r\n'
                dest.write(line)


if __name__ == '__main__':
    unix2dos(sys.argv[1])
