#!/usr/bin/env python3
import time
import pickle
import menu

benjin = {'foundation': 10000}


def mianmenu():
    cmds = {'1': shouru, '2': zhichu, '3': chazhang, '4': gaizhang}
    select = menu.menu('''请选择您需要的操作
1. 收入\t\t2. 支出
3. 查询\t\t4. 修改
5. 退出
''', '12345')
    while True:
        if select == '5':
            print('感谢使用')
        cmds[select]()


def shouru():
    while True:
        money = int(input('请输入金额： '))
        stime = time.time()
        confirm = input('您本次的收入是：%s，您确定吗y？' % money)
        if confirm != 'y':
            print('重新输入')
            continue
        beizhu = input('请输入备注： ')
        break
    with open('/tmp/jizhang.txt', 'ab') as f2:
        pickle.dump({'id': id_get(), 'time': stime, 'money': money, '类型': '收入', 'type': 1, '说明': beizhu}, f2)



def zhichu():
    while True:
        money = int(input('请输入金额： '))
        stime = time.time()
        confirm = input('您本次的支出是：%s，您确定吗y？' % money)
        if confirm != 'y':
            print('重新输入')
            continue
        beizhu = input('请输入备注： ')
        break
    with open('/tmp/jizhang.txt', 'ab') as f2:
        pickle.dump({'id': id_get(), 'time': stime, 'money': money, '类型': '收入', 'type': -1, '说明': beizhu}, f2)


def chazhang():
    select = menu.menu('''请选择你需要查询的内容
1. 明细\t\t2. 结余
''', '12')
    while True:
        if select == 1:


def gaizhang():
    print()


def jieyu():
    print()


def id_get():
    with open('/tmp/.id.txt') as f1:
        id = f1.read()
        return id


def id_input():
    id = id_get()
    with open('/tmp/.id.txt', 'w') as f1:
        id = int(id) + 1
        f1.write(id)


if __name__ == '__main__':
    menu()