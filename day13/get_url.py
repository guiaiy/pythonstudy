#!/usr/bin/env python3
import os
import re
from urllib import request, error


def download(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as f1:
        while True:
            data = html.read(4096)
            if not data:
                break
            f1.write(data)


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
    fname = '/tmp/163.html'
    pic_patt = '(http|https)://.*\.(png|jpg|jpeg|gif)'
    download(net_url, fname)
    pic_list = get_url(fname, pic_patt, encoding='gbk')
    folder = '/tmp/wangyi/'
    if not os.path.exists(folder):
        os.mkdir(folder)
    for url in pic_list:
        pic_name = os.path.basename(url)
        try:
            download(url, folder + pic_name)
        except error.HTTPError:
            print(url)
