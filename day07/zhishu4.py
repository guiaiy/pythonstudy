#!/usr/bin/env python3
import datetime

while True:
    try:
        num = int(input('请输入一个大于2的数字,将输出它以内的所有质数:  '))
    except ValueError:
        continue
    if num < 2:
        continue
    break

begin = datetime.datetime.now()
num_list = []

for i in range(2, int(num+1)//1+1):
    num_list.append(i)

while len(num_list) > 1 and num_list[0] ** 2 < num_list[-1]:
    print(num_list[0], end=', ')
    num_list = list(filter(lambda x: x % num_list[0], num_list))

for i in num_list:
    if i != num_list[-1]:
        print(i, end=', ')
    else:
        print(i)

finish = datetime.datetime.now()
print('程序一共花了 %s 秒' % (finish - begin).seconds)

