from urllib import request, error

url1 = 'http://176.52.10.170/ban/'
url2 = 'http://176.52.10.170/'
# html = request.urlopen(url2)
for url in [url1, url2]:
    try:
        html = request.urlopen(url)
    except error.HTTPError as e:
        print('错误: ', e)
    else:
        data = html.read()
        print(data)
