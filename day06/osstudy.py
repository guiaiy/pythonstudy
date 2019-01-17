import os

os.listdir()
try:
    os.mkdir('/tmp/demo')
    os.symlink('/etc/hosts', '/tmp/demo/hosts')
    os.mknod('hi.txt')
except FileExistsError:
    print('目录已经存在')

os.chdir('/tmp/demo')

print(os.listdir('/tmp'))

