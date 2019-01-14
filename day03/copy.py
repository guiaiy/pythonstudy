###将/bin/ls复制到/tmp/list
with open('/bin/ls','rb') as f1:
    with open('/tmp/list','wb')as f2:
        data=f1.read(4096)
        while data:
            f2.write(data)
            data=f1.read(4096)