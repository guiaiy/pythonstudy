import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.11', username='root', password='123456')
ssh.exec_command('mkdir /root/haha')
ssh.close()
