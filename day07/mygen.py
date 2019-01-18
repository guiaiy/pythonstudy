#!/usr/bin/env python3


def mygen():
    yield 10
    a = 100 + 200
    yield a
    yield 'hello'


if __name__ == '__main__':
    a = mygen()
    for i in a:
        print(i)
