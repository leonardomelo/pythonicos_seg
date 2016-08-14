#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import OrderedDict

logs = '''
64.242.88.10 - - [07/Mar/2004:16:05:49 -0800] "GET /twiki/bin/edit/Main/Double_bounce_sender?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12846
64.242.88.10 - - [07/Mar/2004:16:06:51 -0800] "GET /twiki/bin/rdiff/TWiki/NewUserTemplate?rev1=1.3&rev2=1.2 HTTP/1.1" 200 4523
64.242.88.10 - - [07/Mar/2004:16:10:02 -0800] "GET /mailman/listinfo/hsdivision HTTP/1.1" 200 6291
64.242.88.10 - - [07/Mar/2004:16:11:58 -0800] "GET /twiki/bin/view/TWiki/WikiSyntax HTTP/1.1" 200 7352
64.242.88.10 - - [07/Mar/2004:16:20:55 -0800] "GET /twiki/bin/view/Main/DCCAndPostFix HTTP/1.1" 200 5253
64.242.88.10 - - [07/Mar/2004:16:23:12 -0800] "GET /twiki/bin/oops/TWiki/AppendixFileSystem?template=oopsmore¶m1=1.12¶m2=1.12 HTTP/1.1" 200 11382
64.242.88.10 - - [07/Mar/2004:16:24:16 -0800] "GET /twiki/bin/view/Main/PeterThoeny HTTP/1.1" 200 4924
64.242.88.10 - - [07/Mar/2004:16:29:16 -0800] "GET /twiki/bin/edit/Main/Header_checks?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12851
64.242.88.10 - - [07/Mar/2004:16:30:29 -0800] "GET /twiki/bin/attach/Main/OfficeLocations HTTP/1.1" 401 12851
64.242.88.10 - - [07/Mar/2004:16:31:48 -0800] "GET /twiki/bin/view/TWiki/WebTopicEditTemplate HTTP/1.1" 200 3732
64.242.88.10 - - [07/Mar/2004:16:32:50 -0800] "GET /twiki/bin/view/Main/WebChanges HTTP/1.1" 200 40520
64.242.88.10 - - [07/Mar/2004:16:33:53 -0800] "GET /twiki/bin/edit/Main/Smtpd_etrn_restrictions?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12851
64.242.88.10 - - [07/Mar/2004:16:35:19 -0800] "GET /mailman/listinfo/business HTTP/1.1" 200 6379
64.242.88.10 - - [07/Mar/2004:16:36:22 -0800] "GET /twiki/bin/rdiff/Main/WebIndex?rev1=1.2&rev2=1.1 HTTP/1.1" 200 46373
64.242.88.10 - - [07/Mar/2004:16:37:27 -0800] "GET /twiki/bin/view/TWiki/DontNotify HTTP/1.1" 200 4140
64.242.88.10 - - [07/Mar/2004:16:39:24 -0800] "GET /twiki/bin/view/Main/TokyoOffice HTTP/1.1" 200 3853
64.242.88.10 - - [07/Mar/2004:16:43:54 -0800] "GET /twiki/bin/view/Main/MikeMannix HTTP/1.1" 200 3686
64.242.88.10 - - [07/Mar/2004:16:45:56 -0800] "GET /twiki/bin/attach/Main/PostfixCommands HTTP/1.1" 401 12846
'''

'''modo rápido de fazer'''
for log in logs.split('\n'):
    log = log.split()
    if log:
        dicio = OrderedDict([('Data',log[3].split(':')[0].replace('[','')),('Hora',':'.join(log[3].split(':')[1:4])), ('IP',log[0]),('Metodo',log[5].replace('"','')),('Caminho',log[6]),('Resposta',log[8]),('Tamanho',log[9])])
        print '-'*100
        for key,value in dicio.items():
            if key is not 'Resposta':
                print '%s\t\t%s'%(key,value)
            else:
                print '%s\t%s'%(key,value)

'''
loga = []
for log in logs.split('\n'):
    log = log.split()
    loga.append(log)

del loga[0]
del loga[len(loga)-1]

dicio = OrderedDict()
lista = []

for x in loga:
    del x[1]
    del x[1]
    x[1] = x[1].replace('[','')
    x[2] = x[2].replace(']','')
    x[3] = x[3].replace('"','')
    x[5] = x[5].replace('"','')

for x in loga:
    dicio['Data'] = x[1][0:11]
    dicio['Hora'] = x[1][12:20]
    dicio['IP'] = x[0]
    dicio['Metodo'] = x[3]
    dicio['Caminho'] = x[4]
    dicio['Resposta'] = x[6]
    dicio['Tamanho'] = x[7]
    lista.append(dicio.copy())
'''
'''Imprime na tela a lista de dicionários'''
'''
for x in lista:
    for key,value in x.items():
        if key == 'Data' or key == 'Hora' or key == 'IP' or key == 'Metodo':
            print key,'\t\t', value
        else:
            print key,'\t', value
    print '-'*100
'''
