#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def recursividade(diretorio,base):
    print base
    for item in os.listdir(diretorio):
        if os.path.isdir:
            print '----' + item
    print '-'*65
    for item in os.listdir(diretorio):
        itemConcat = os.path.join(diretorio,item)
        if os.path.isdir(itemConcat):
            base = os.path.join(base,os.path.basename(itemConcat))
            recursividade(itemConcat,base)

recursividade(os.getcwd(),'./')

'''
descrição da solução:

    1ª tentativa:
        fiz sem concatenar, passando, no if, os.path.isdir(item)
        resultado: na segunda passada, ele não detectava nenhum diretório Oo

    2ª tentativa:
        quando retirava o item, concatenei com o diretório original pra ver se reconheceria como diretório na segunda passada
        resultado: reconheceu e terminei o desafio

obs:
    o "./" foi só pra ficar parecido com o "ls -R"
    o "base" é só pra ficar parecido com o "ls -R"
    tentei colorir o print dos diretórios, mas desisti depois
'''
