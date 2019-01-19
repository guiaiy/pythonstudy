#!/usr/bin/env python3
import datetime


def time_contro(func):
    def time_spend():
        begin = datetime.datetime.now()
        print(func())
        finish = datetime.datetime.now()
        return (finish - begin).seconds
    return time_spend


def num_input():   ###输入一个数字，输出数字（包含）以内的所有质数
    while True:
        try:
            num = int(input('请输入一个大于2的数字,将输出它以内所有质数:  '))
        except ValueError:
            continue
        if num < 2:
            continue
        break
    return num


def num_save(): ### 将数字存入列表
    zhishu_list1 = []
    for i in range(2, int(num_input())//1+1):
        zhishu_list1.append(i)
    return zhishu_list1


@time_contro
def num_filter(): ### 过滤非质数，根据数学原理，循环不需超过最大数的平方根
    num_list = num_save()
    zhishu_list = []
    while len(num_list) > 1 and num_list[0] ** 2 < num_list[-1]:
        zhishu_list.append(num_list[0])
        num_list = list(filter(lambda x: x % num_list[0], num_list))
    return zhishu_list + num_list


if __name__ == '__main__':
    print(num_filter())
