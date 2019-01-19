#!/usr/bin/env python3
import time


def deco(func1, func2):
    def timeit():
        start = time.time()
        yield func1()
        yield func2()
        end = time.time()
        yield end - start

    return timeit


def myadd():
    res = 0
    for i in range(10000000):
        res += i
    return res


def myadd2():
    res2 = 0
    for i in range(10000000):
        res2 += i
    return res2


if __name__ == '__main__':
    a = deco(myadd, myadd2)
    for i in a():
        print(i)
