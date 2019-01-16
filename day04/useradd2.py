import sys
import randpass2
import subprocess

def adduser(username,password,userfile):
    user_info='''username:%s
password:%s
''' % (username,password)
    subprocess.call(
        'useradd %s' % username,shell=True
    )
    subprocess.call(
        'echo %s | passwd --stdin %s' % (password,username),shell=True
    )
    with open(userfile,'a') as fobj:
        fobj.write(user_info)

if __name__ == '__main__':
    password = randpass2.getrandpass2()
    adduser(sys.argv[1],password,'/tmp/passwd')
