import user

if __name__ == '__main__':
    select = input('请选择一个功能1，注册 2，登录\n')
    if select == '1':
        user.infosave()
    if select == '2':
        user.login()
