#!/usr/bin/env python3
import checkid
import getpass


userdb = {}


def user_regist():
    print('用户注册')
    while True:
        username = input('请输入用户名\n')
        check = user_check(username)
        result = checkid.check_id(username)
        if check == 'false':
            username = input('用户名已经存在，请重新输入用户名\n')
            continue
        if result != 0:
            continue
    while True:
        password = getpass.getpass('请输入密码,密码必须超过八位，包括大小写字母和数字\n')
        check = pass_check(password)
        if check != '0':
            continue
    userdb.update({username:password})
    print('注册成功')


def user_check(username):
    for user in userdb:
        if username == user:
            return 'false'
    return 'true'


def password_check(username,password):
    with open('/var/www/userinfosave') as f1:
        lines = f1.readlines()
        for line in lines:
            user = line.replace(line[line.index(':'):],'')
            userpass = line.replace(line[0:line.index(':')+1],'')
            if user == username and userpass == password+'\n':
                return 'true'
        return 'false'


def login():
    print('用户登录')
    username = input('请输入用户名\n')
    password = getpass.getpass('请输入密码\n')
    userchec = usercheck(username)
    passchec = passwordcheck(username,password)
    false = 0
    while userchec == 'true' and false < 3:
        username = input('用户名不存在，请重新输入\n')
        userchec = usercheck(username)
        password = getpass.getpass('请输入密码\n')
        passchec = passwordcheck(username, password)
        false += 1
    while passchec == 'false' and false < 3:
        print('密码错误，请重新输入')
        password = getpass.getpass('请输入密码\n')
        passchec = passwordcheck(username,password)
        false += 1
    if false >= 3:
        print('失败次数过多，退出程序')
        return 'false'
    print('登录成功')
    with open('/var/www/'+username+'longinfo','w') as f2:
        f2.write('login\n')


def pass_check(password):
    print()


if __name__ == '__main__':
    user_regist()