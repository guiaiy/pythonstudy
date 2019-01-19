#!/usr/bin/env python3
import datetime


def num_input():  ###输入一个数字，输出数字（包含）以内的所有质数
    while True:
        try:
            num = int(input('请输入一个大于2的数字,将输出它以内的所有质数:  '))
        except ValueError:
            continue
        if num < 2:
            continue
        break
    return num


def num_save(num):  ### 将数字存入列表
    zhishu_list1 = []
    for i in range(2, int(num + 1) // 1 + 1):
        zhishu_list1.append(i)
    return zhishu_list1


def num_filter(num_list):  ### 过滤非质数，根据数学原理，循环不需超过最大数的平方根
    while len(num_list) > 1 and num_list[0] ** 2 < num_list[-1]:
        print(num_list[0], end=', ')
        num_list = list(filter(lambda x: x % num_list[0], num_list))
    for i in num_list:
        if i != num_list[-1]:
            print(i, end=', ')
        else:
            print(i)


if __name__ == '__main__':
    num = num_input()
    print('%s以内的质数有:  ' % num)
    numlist = num_save(num)
    begin = datetime.datetime.now()
    # num_filter(numlist)
    finish = datetime.datetime.now()
    print('程序一共花了 %s 秒' % (finish - begin).seconds)
