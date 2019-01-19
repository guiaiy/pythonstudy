#!/usr/bin/env python3


def deco(func):
    def color():
        return '\033[31;1m%s\033[1m' % func()

    return color


def hello():
    return 'hello world'


@deco
def welcome():
    return 'hello china'


if __name__ == '__main__':
    hello = deco(hello)
    print(hello())
    print(welcome())
