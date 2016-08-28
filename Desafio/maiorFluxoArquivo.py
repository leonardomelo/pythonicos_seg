#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from collections import OrderedDict

def zeraArquivo(dicionario):
    f = open('resultado.txt','w')
    f.write('')
    f.close()

def adicionaAoArquivo(dicionario):
    f = open('resultado.txt','a')
    for key,value in dicionario.items():
        f.write(key)
        f.write('    ')
        f.write('\t')
        f.write(str(value))
        f.write('Mb')
        f.write('\n')
    f.close()

def imprimeArquivo():
    print('\nLeitura do arquivo\n')
    f = open('resultado.txt')
    print f.read()
    f.close()

def bitsParaMb(dicionario):
    for key,value in dicionario.items():
        dicionario[key] = float("{0:.3f}".format(value/1024/1024))
    return dicionario

def ordenaDicio(dicionario):
    dicio_aux = dicionario;
    dicionario = sorted(dicionario.values())
    dicionario = dicionario[::-1]
    dicio_resultado = OrderedDict()
    for i in dicionario:
        for key,value in dicio_aux.items():
            if value == i:
                dicio_resultado[key] = value
    return dicio_resultado

def filtraLogsSomaValores(arqlogs,dicionario):
    f = open(arqlogs)
    logs = f.readlines()
    f.close()
    if logs:
        for log in logs:
            log = log.split()
            if os.path.basename(arqlogs) not in dicionario.keys():
                dicionario[os.path.basename(arqlogs)] = float(log[9])
            else:
                dicionario[os.path.basename(arqlogs)] = float(dicionario[os.path.basename(arqlogs)]) + float(log[9])
    else:
        dicionario[os.path.basename(arqlogs)] = 0
    return dicionario

def recursividadeDiretorios(diretorio,base,dicionario):
    print base
    for item in os.listdir(diretorio):
        nitem = os.path.join(diretorio,item)
        print '---',item
        if os.path.isfile(nitem):
            if item[0] == 'l' and item[1] == 'o' and item[2] == 'g':
                dicionario = filtraLogsSomaValores(nitem,dicionario)
    for item in os.listdir(diretorio):
        nitem = os.path.join(diretorio,item)
        if os.path.isdir(nitem):
            dicionario = recursividadeDiretorios(nitem,os.path.join(base,item),dicionario)
    try:
        return dicionario
    except:
        return 'Dicionário vazio'

def __main():
    print '\nLeitura da estrutura de diretórios\n'
    dicio = recursividadeDiretorios(os.getcwd(),'./', dict())
    print '-'*100
    if dicio == 'Dicionário vazio':
        print dicio
    else:
        dicio = ordenaDicio(dicio)
        dicio = bitsParaMb(dicio)
        zeraArquivo(dicio)
        adicionaAoArquivo(dicio)
        imprimeArquivo()

__main()
