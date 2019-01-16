import randpass2
import check

def user_create():
    while True:
        username=input('please input user username: ')
        result=check.check_id(username)
        if result != '\033[32;1mvalid\033[0m':
            print(check.check_id(username))
        else:
            passwd=randpass2.getrandpass2(8)
            break
    return '%s:%s'%(username,passwd)

def userinfo_save(userinfo):
    with open('/tmp/passwd','a') as user:
        user.write(str(userinfo)+'\n')

if __name__ == '__main__':
    result=str(user_create())
    userinfo_save(str(result))