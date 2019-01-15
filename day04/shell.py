import  shutil

##copyfileobj必须事先打开文件
f1=open('/tmp/passwd')
f2=open('/tmp/list2.txt','w')
shutil.copyfileobj(f1,f2) 

##无需事先打开文件
shutil.copy('/etc/hosts','/tmp/zj.txt') 

##源和目标都必须是文件
shutil.copyfile('/etc/hosts','/tmp/zhuji.txt') 

##目标可以是目录
shutil.copy('/etc/hosts','/tmp/')

##拷贝目录，目标必须是新目录
# shutil.copytree('/etc/security','/tmp/anquan')

shutil.move('/tmp/zhuji.txt','/tmp/zhuji')

##没有rm方法，只有rmtree
shutil.rmtree('/tmp/anquan')
help(shutil)
