import checkid
import getpass

def useradd():
    print('用户注册')
    username = input('请输入用户名\n')
    check = usercheck(username)
    result = checkid.check_id(username)
    while check == 'false' or result != 0:
        if check == 'false':
            username = input('用户名已经存在，请重新输入用户名\n')
            check = usercheck(username)
            result = checkid.check_id(username)
        if result != 0:
            username = input('请重新输入用户名\n')
            result = checkid.check_id(username)
    password = getpass.getpass('请输入6位以上密码\n')
    while len(password) < 6:
        password = getpass.getpass('密码长度不够，请重新输入\n')
    return {username:password}

def infosave():
    with open('/tmp/userinfosave','a') as f1:
        userinfo = useradd()
        for user in userinfo:
            info = user+':'+userinfo[user]
            f1.write(info+'\n')

def usercheck(username):
    with open('/tmp/userinfosave') as f1:
        userinfo = f1.readlines()
        for line in userinfo:
            user = line.replace(line[line.index(':'):],'')
            if username == user:
                return 'false'
        return 'true'

def passwordcheck(username,password):
    with open('/tmp/userinfosave') as f1:
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
        passchec = getpass.getpass('请输入密码\n')
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
    with open('/tmp/'+username+'longinfo','w') as f2:
        f2.write('login')




if __name__ == '__main__':
    login()