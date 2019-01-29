from urllib import request

html = request.urlopen('http://www.baidu.com')
with open('/tmp/baidu.html', 'wb') as f1:
    while True:
        data = html.read(4096)
        if data:
            f1.write(data)
        else:
            break
