#!/usr/bin/env python3
import time


def rail_way():
    print('#' * 20, end='')
    n = 0
    while True:
        time.sleep(0.3)
        print('\r%s@%s' % ('#' * n, '#' * (19-n)), end='')
        n += 1
        if n == 20:
            n = 0

if __name__ == '__main__':
    rail_way()