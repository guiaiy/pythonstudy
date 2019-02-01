import json
from urllib import request

html = request.urlopen('http://www.weather.com.cn/data/sk/101250101.html')
data = html.read()
info = json.loads(data)
# pprint.pprint(info)
print(info['weatherinfo']['city'])
