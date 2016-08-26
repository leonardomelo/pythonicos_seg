#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def filtraLogs(arqlogs):
    f = open(arqlogs)
    logs = f.readlines()
    f.close()
    # print len(logs)
    if logs:
        for log in logs:
            print log
        # print logs[1]
    # print arqlogs

def recursividadeLogs(diretorio,base):
    print base
    for item in os.listdir(diretorio):
        nitem = os.path.join(diretorio,item)
        print '---',item
        if os.path.isfile(nitem) and item.split('.')[1] == 'txt':
            # print nitem
            filtraLogs(nitem)
    print '-'*100
    for item in os.listdir(diretorio):
        nitem = os.path.join(diretorio,item)
        if os.path.isdir(nitem):
            recursividadeLogs(nitem,os.path.join(base,item))

recursividadeLogs(os.getcwd(),'./')
