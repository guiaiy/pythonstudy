#!/usr/bin/env python3
from day05 import user

if __name__ == '__main__':
    while True:
        cmds = {'1': user.infosave, '2': user.login}
        select = input('请选择一个功能1，注册 2，登录 3,退出\n').strip()
        if not select:
            print('输入有误，请重新输入')
            continue
        select = select[0]
        if select not in '123':
            print('输入有误，请重新输入')
            continue
        if select == '3':
            exit()
        cmds[select]()
        # if select == '1':
        #     user.infosave()
        # if select == '2':
        #     user.login()
