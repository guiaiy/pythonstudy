#!/usr/bin/env python3
from random import randint

def jiecheng(x):
    if x == 1:
        return 1
    return x * jiecheng(x - 1)


def chitangguo(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 4
    return chitangguo(x - 1) + chitangguo(x - 2) + chitangguo(x - 3)


def qsort(seq):
    if len(seq) < 2:
        return seq
    smaller = []
    lager = []
    # for i in range(1, len(seq)):
    #     if seq[i] < seq[0]:
    #         smaller.append(seq[i])
    #     else:
    #         lager.append(seq[i])
    # return qsort(smaller) + [seq[0]] + qsort(lager)
    for num in seq[1:]:
        if num < seq[0]:
            smaller.append(num)
        else:
            lager.append(num)
    return qsort(smaller) + [seq[0]] + qsort(lager)



if __name__ == '__main__':
    print(jiecheng(5))
    print(chitangguo(10))
    nums = [randint(1, 10000) for i in range(1000)]
    print(qsort(nums))
