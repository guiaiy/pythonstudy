#!/usr/bin/env python3
import datetime

###输入一个数字，输出数字（包含）以内的所有质数
num=int(input('please input a number:  '))
zhishu=[]

begin=datetime.datetime.now()
### 将质数存入数组
for i in range(2,num+1):
    zhishu.append(i)

while len(zhishu) < 1 and zhishu[0] ** 2 > zhishu[-1]:
    print(zhishu[0])
    zhishu = list(filter(lambda x: x % zhishu[0], zhishu))


for i in zhishu:
    if i !=zhishu[-1]:
        print(i, end=', ')
print(zhishu[-1], end='')

finish=datetime.datetime.now()

### 换行
print()

### 统计运行时间
print((finish-begin).seconds)

