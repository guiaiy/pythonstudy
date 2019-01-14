###以r方式打开文件
passwd=open('/tmp/passwd')
data=passwd.read()
print(data)
data=passwd.read()
print(data)
passwd.close()

passwd=open('/tmp/passwd')
passwd.readlines(1)

passwd=open('/tmp/passwd')
for line in passwd:
    print(line,end='')

###以w方式打开文件,文件存在则清空
passwd=open('/tmp/passwd','w')
passwd.write('Hello World!\n')  ##数据写入内存
passwd.flush()  ##立即将数据写入磁盘
passwd.writelines(['heihei,\n','haha\n'])
passwd.close()  ##也会立即将数据写入磁盘

###with语句打开文件后，with语句结束，文件自动关闭
with open('tmp/passwd') as passwd:
    passwd.readlines()

###指针
passwd=open('/tmp/passwd')
passwd.seek(6,0)
