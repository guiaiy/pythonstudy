import checkid
import getpass

def useradd():
    username = input('请输入用户名\n')
    result = checkid.check_id(username)
    while result != 0:
        username = input('请重新输入用户名\n')
        result = checkid.check_id(username)
    password = getpass.getpass('请输入6位以上密码\n')
    while len(password) < 6:
        password = getpass.getpass('密码长度不够，请重新输入\n')
    return (username,password)

def infosave():
    with open('/tmp/userinfosave','a') as f1:
        userinfo = useradd()
        for user,passwd in userinfo:
            strinfo=user+':'+passwd
            f1.write(strinfo)
        return userinfo


if __name__ == '__main__':
    userinfo=infosave()
    print(userinfo)