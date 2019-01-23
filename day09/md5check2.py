#!/usr/bin/env python3
import os
import pickle
import tarfile
from time import strftime

from md5check import check_md5


def afname_get(dname):
    dir = os.walk(dname)
    filelist = []
    for path, folder, files in dir:
        for file in files:
            afname = os.path.join(path, file)
            filelist.append(afname)
    return filelist


def md5_save(dname):
    savelist = afname_get(dname)
    savedic = {}
    for file in savelist:
        md5 = check_md5(file)
        savedic.update({file: md5})
    with open(os.path.join('/tmp/backups/' + os.path.basename(dname.rstrip('/')), 'md5.txt'), 'wb') as f1:
        pickle.dump(savedic, f1)


def oldmd5_get(dname):
    with open(os.path.join('/tmp/backups/' + os.path.basename(dname.rstrip('/')), 'md5.txt'), 'rb') as f1:
        md5dic = pickle.load(f1)
    return md5dic


def md5_check2(dname):
    filelists = afname_get(dname)
    oldmd5dic = oldmd5_get(dname)
    incr_files = []
    for file in filelists:
        fmd5 = check_md5(file)
        if not oldmd5dic.get(file):
            incr_files.append(file)
        elif oldmd5dic[file] != fmd5:
            incr_files.append(file)
    return incr_files


def fullbackup(dname):
    if not os.path.exists('/tmp/backups'):
        os.mkdir('/tmp/backups')
    if not os.path.exists('/tmp/backups/' + os.path.basename(dname.rstrip('/'))):
        os.mkdir('/tmp/backups/' + os.path.basename(dname.rstrip('/')))
    os.chdir('/tmp/backups/' + os.path.basename(dname.rstrip('/')))
    fname = '%s_full_%s.tar.gz' % (os.path.basename(dname.rstrip('/')), strftime('%Y%m%d'))
    tar = tarfile.open(fname, 'w:gz')
    tar.add(dname)
    tar.close()
    md5_save(dname)


def incr_backup(dname):
    incrfiles = md5_check2(dname)
    if incrfiles:
        os.chdir('/tmp/backups/' + os.path.basename(dname).rstrip('/'))
        fname = '%s_incr_%s.tar.gz' % (os.path.basename(dname.rstrip('/')), strftime('%Y%m%d'))
        tar = tarfile.open(fname, 'w:gz')
        for file in incrfiles:
            tar.add(file)
        tar.close()
        md5_save(dname)


if __name__ == '__main__':
    dname = '/mnt'
    if strftime('%a') == 'Mon':
        fullbackup(dname)
    else:
        incr_backup(dname)

    # print('%s_full_%s.tar.gz' % (os.path.basename('/mnt/abcd/'.rstrip('/')), strftime('%Y%m%d')))
