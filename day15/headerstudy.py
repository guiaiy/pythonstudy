import requests

header = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
r = requests.get('http://127.0.0.1/', headers=header)
r = requests.get('http://127.0.0.1')
print(r.status_code)

r = requests.get('http://127.0.0.1/abc')
print(r.status_code)
print(r.raise_for_status())
