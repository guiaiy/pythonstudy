#!/usr/bin/env python3
import hashlib
import os
import tarfile

import requests
import wget


def has_new_version(live_url, live_fname):
    if not os.path.isfile(live_fname):
        return True  # 本地没有版本文件，意味着有新版本

    with open(live_fname) as f1:
        local_version = f1.read()
    r = requests.get(live_url)
    if r.text != local_version:
        return True  # 本地版本和服务器版本不一样，意味着有新版本

    return False  # 如果以上判断都不成立，意味着没有新版本


def md5sum(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as f1:
        while True:
            data = f1.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()


def deploy(app_fname, deploy_dir):
    tar = tarfile.open(app_fname, 'r:gz')
    tar.extractall(deploy_dir)
    tar.close()
    app_path = os.path.basename(app_fname)
    app_path = app_path.replace('.tar.gz', '')
    app_path = os.path.join(deploy_dir, app_path)
    dest_path = 'nsd1808'
    if os.path.exists(dest_path):
        os.unlink(dest_path)
    os.symlink(app_path, dest_path)


if __name__ == '__main__':
    live_url = 'http://39.108.76.244/deploy/live_version'
    live_fname = 'deploy/live_version'
    if not has_new_version(live_url, live_fname):
        print('没有新版本')
        exit()
    r = requests.get(live_url)
    deploy_dir = 'deploy'
    download_dir = 'download'
    app_url = 'http://39.108.76.244/deploy/packages/mysite_%s.tar.gz' % (r.text.strip())
    wget.download(app_url, download_dir)  # 下载压缩包
    app_md5_url = app_url + '.md5'
    wget.download(app_md5_url, download_dir)  # 下载MD5文件
    if os.path.exists(live_fname):
        os.remove(live_fname)
    wget.download(live_url, deploy_dir)  # 下载版本文件
    app_fname = os.path.join(download_dir, app_url.split('/')[-1])
    local_md5 = md5sum(app_fname)
    r = requests.get(app_md5_url)
    if local_md5 != r.text.strip():
        print('文件校验失败')
        exit(1)
    deploy(app_fname, deploy_dir)
