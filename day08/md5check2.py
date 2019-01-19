#!/usr/bin/env python3
import os
from md5check import md5_check
import pickle


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
        md5 = md5_check(file)
        savedic.update({file: md5})
    with open(os.path.join(dname, 'md5.txt'), 'wb') as f1:
        pickle.dump(savedic, f1)

def oldmd5_get(dname):
    with open(os.path.join(dname, 'md5.txt'), 'rb') as f1:
        md5dic = pickle.load(f1)
    return md5dic



def md5_check2(dname):
    filelists = afname_get(dname)
    oldmd5dic = oldmd5_get(dname)
    for file in filelists:
        fmd5 = md5_check(file)



if __name__ == '__main__':
