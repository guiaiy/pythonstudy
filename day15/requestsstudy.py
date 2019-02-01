import requests

r = requests.get('http://www.sogou.com')
print(r.text)

jgp = requests.get('http://g.hiphotos.baidu.com/image/h%3D300/sign=ea5d1597e6f81a4c3932eac9e72b6029/2e2eb9389b504fc2330c17e6e8dde71191ef6d86.jpg')

with open('./m.jpg', 'wb') as f1:
    f1.write(jgp.content)

html = requests.get('http://www.weather.com.cn/data/sk/101250101.html')
html.encoding = 'utf8'
info = html.json()
print(info)


url = 'https://www.sogou.com/web'
param = {'query': '人民币汇率'}
r = requests.get(url, params=param)
with open('sogou.html', 'w') as f1:
    f1.write(r.text)
