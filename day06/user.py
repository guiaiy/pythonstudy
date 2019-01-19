#!/usr/bin/env python3
import getpass

import checkid

userdb = {}
loginfo = {}


def user_regist():
    print('用户注册')
    while True:
        username = input('请输入用户名\n')
        check = user_check(username)
        result = checkid.check_id(username)
        if check == 'false':
            print('用户名已经存在，请重新输入用户名\n')
            continue
        if result != 0:
            continue
        else:
            break
    while True:
        password = getpass.getpass('请输入密码,密码必须超过八位，包括字母和数字\n')
        check = pass_check(password)
        if check != 0:
            continue
        userdb.update({username: password})
        print('注册成功')


def user_check(username):
    for user in userdb:
        if username == user:
            return 'false'
    return 'true'


def password_check(username, password):
    for user, userpass in userdb.items():
        if user == username and userpass == password:
            return 'true'
    return 'false'


def login():
    false = 0
    while True:
        print('用户登录')
        username = input('请输入用户名\n')
        password = getpass.getpass('请输入密码\n')
        userchec = user_check(username)
        passchec = password_check(username, password)
        if userchec == 'true' and false < 3:
            print('用户名不存在，请重新输入\n')
            false += 1
            continue
        if passchec == 'false' and false < 3:
            print('密码错误，请重新输入')
            false += 1
            continue
        if false >= 3:
            print('失败次数过多，退出程序')
            return 'false'
        print('登录成功')
        loginfo.update({username: 'login'})


def pass_check(password):
    if len(password) < 8:
        print('密码长度不够')
        return 1
    if password.isdigit():
        print('密码不能为纯数字')
        return 2
    count = 0
    for i in password:
        if i.isdigit():
            count += 1
    if count == 0:
        print('密码必须包含数字')
        return 3
    return 0


if __name__ == '__main__':
    user_regist()
