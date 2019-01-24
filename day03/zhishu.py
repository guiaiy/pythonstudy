import datetime

# 输入一个数字，输出数字（包含）以内的所有质数
num = int(input('please input a number:  '))
zhishu = []

begin = datetime.datetime.now()
# 将质数存入数组
for i in range(2, num + 1):
    zhishu.append(i)

# 将数组内非质数剔除
for i in range(2, int(zhishu[-1] ** 0.5) + 1):  # 当zhishu[-1]//2+1 < 3的时候有一点bug
    if len(zhishu) > 1:
        print(zhishu[0], end=', ')
        del zhishu[0]
        for j in zhishu:
            if j % i == 0:
                zhishu.remove(j)
    else:
        print(zhishu[0], end='')
        del zhishu[0]
        break

# 修复zhishi[-1]/2+1 < 3 的bug
for i in zhishu:
    if i != zhishu[-1]:
        print(i, end=', ')
    else:
        print(i, end='')

finish = datetime.datetime.now()

# 换行
print()

# 统计运行时间
print((finish - begin).seconds)
