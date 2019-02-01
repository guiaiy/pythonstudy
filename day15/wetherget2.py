import requests
# import json
import pprint

html = requests.get('http://www.weather.com.cn/data/sk/101250101.html')
html.encoding = 'utf8'
info = html.json()
pprint.pprint(info)
print(info['weatherinfo']['SD'])
