#!/usr/bin/python
#coding:utf8

import os

def dirList(path):
    filelist = os.listdir(path)
    fpath = os.getcwd()
    allfile = []
    for filename in filelist:
        filepath = os.path.join(path,filename)
        if os.path.isdir(filepath):
            allfile.append(dirList(filepath))
        allfile.append(filepath)
    return allfile
allfile = dirList('tmp')
print allfile


