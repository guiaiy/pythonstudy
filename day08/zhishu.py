#!/usr/bin/env python3
import datetime


def time_contro(func):
    def time_spend(arg1):
        begin = datetime.datetime.now()
        print(func(arg1))
        finish = datetime.datetime.now()
        return '程序一共花了 %s 秒' % (finish - begin).seconds
    return time_spend


def num_input():   ###输入一个数字，输出数字（包含）以内的所有质数
    while True:
        try:
            num = int(input('请输入一个大于2的数字,将输出它以内的所有质数:  '))
        except ValueError:
            continue
        if num < 2:
            continue
        break
    return num


def num_save(num): ### 将数字存入列表
    zhishu_list = []
    for i in range(2, int(num+1)//1):
        zhishu_list.append(i)
    return zhishu_list


@time_contro
def num_filter(num_list): ### 过滤非质数，根据数学原理，循环不需超过最大数的平方根
    zhishu_list = []
    while num_list[0] ** 2 <= num_list[-1]:
        zhishu_list.append(num_list[0])
        num_list = list(filter(lambda x: x % num_list[0], num_list))
    return zhishu_list + num_list


if __name__ == '__main__':
    num = num_input()
    print('%s以内的质数有:  ' % num)
    numlist = num_save(num)
    print(num_filter(numlist))
