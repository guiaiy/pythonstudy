from urllib import request

# url = 'https://www.baidu.com/s?wd=%s'
url = 'https://www.sogou.com/web?query=%s'
param = request.quote('中国')
print(param)
html = request.urlopen(url % param)
with open('china.html', 'wb') as f1:
    data = html.read()
    f1.write(data)
