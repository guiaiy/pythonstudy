import os
import re
from urllib import error
import wget


# def download(url, fname):
#     html = request.urlopen(url)
#     with open(fname, 'wb') as f1:
#         while True:
#             data = html.read(4096)
#             if not data:
#                 break
#             f1.write(data)


def get_url(fname, patt, encoding=None):
    url_list = []
    cpatt = re.compile(patt)
    with open(fname, encoding=encoding) as f1:
        for line in f1:
            for m in cpatt.finditer(line):
                url_list.append(m.group())
    return url_list


if __name__ == '__main__':
    net_url = 'http://www.163.com/'
    fname = '163.html'
    wget.download(net_url, fname)
    pic_patt = '(http|https)://.*\.(png|jpg|jpeg|gif)'
    pic_list = get_url(fname, pic_patt, encoding='gbk')
    folder = 'wangyi/'
    if not os.path.exists(folder):
        os.mkdir(folder)
    for url in pic_list:
        pic_name = os.path.basename(url)
        try:
            wget.download(url, folder + pic_name)
        except error.HTTPError:
            print(url)
