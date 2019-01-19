#!/usr/bin/env python3
import os
import pickle
import time

import menu

defaultmoney = {'foundation': 10000}


def mainmenu():
    cmds = {'1': shouru, '2': zhichu, '3': chazhang}
    while True:
        mselect = menu.menu('''请选择您需要的操作
1. 收入\t\t2. 支出
3. 查询\t\t4. 退出
''', "['1', '2', '3', '4']")
        if mselect == '4':
            print('感谢使用')
            exit()
        cmds[mselect]()


def shouru():
    while True:
        money = int(input('请输入金额： '))
        confirm = input('您本次的收入是：%s，您确定吗y？' % money)
        if confirm != 'y':
            print('重新输入')
            continue
        beizhu = input('请输入备注： ')
        break
    with open('/tmp/jizhang.txt', 'ab') as f2:
        pickle.dump(
            {'id': id_get(), 'time': time.strftime('%Y-%m-%d'), 'money': money, '类型': '收入', 'type': 1, '说明': beizhu},
            f2)
        id_input()


def zhichu():
    while True:
        money = int(input('请输入金额： '))
        confirm = input('您本次的支出是：%s，您确定吗y？' % money)
        if confirm != 'y':
            print('重新输入')
            continue
        beizhu = input('请输入备注： ')
        break
    with open('/tmp/jizhang.txt', 'ab') as f2:
        pickle.dump(
            {'id': id_get(), 'time': time.strftime('%Y-%m-%d'), 'money': money, '类型': '支出', 'type': -1, '说明': beizhu},
            f2)
        id_input()


def chazhang():
    while True:
        cselect = menu.menu('''请选择你需要查询的内容
1. 明细\t\t2. 结余\t\t
3. 回主菜单\t4. 退出
''', "['1', '2', '3', '4']")
        if cselect == '3':
            mainmenu()
        if cselect == '4':
            exit()
        with open('/tmp/jizhang.txt', 'rb') as f1:
            if cselect == '1':
                id = id_get()
                print()
                print('id\t\t时间\t\t类型\t\t金额\t\t备注')
                for i in range(int(id)):
                    iolist = pickle.load(f1)
                    print('\033[031;1m%(id)s\t\t%(time)s\t%(类型)s\t\t%(money)s\t\t%(说明)s\033[0m' % iolist)
                print()
                continue
            if cselect == '2':
                print('\033[031;1m您的余额是 %s\033[0m' % jieyu())
                continue


def jieyu():
    with open('/tmp/jizhang.txt', 'rb') as f1:
        count = defaultmoney['foundation']
        id = id_get()
        for i in range(id):
            iolist = pickle.load(f1)
            if iolist['type'] == 1:
                count += iolist['money']
            if iolist['type'] == -1:
                count -= iolist['money']
        return count


def id_get():
    if not os.path.exists('/tmp/.id.txt'):
        os.mknod('/tmp/.id.txt')
    with open('/tmp/.id.txt') as f1:
        id = f1.read()
        if not id:
            id = 0
        return int(id)


def id_input():
    id = id_get()
    with open('/tmp/.id.txt', 'w') as f1:
        id = int(id) + 1
        f1.write(str(id))


if __name__ == '__main__':
    mainmenu()
