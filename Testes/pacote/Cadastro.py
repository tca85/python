#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 11, 2016

@author: tca85
'''
import datetime


class Cadastro():
    #-----------------------------------------------------------------------------------------
    def nome(self, nomes):
        print 'Digite o nome:'
        nome = raw_input()
        
        nomes.append(nome)

    #-----------------------------------------------------------------------------------------
    def verificarAnoNascimento(self):
        # raw_input recebe uma string, por isso precisa converter
        print 'Informe sua idade:'
        idade = raw_input()
        
        return int(idade) - datetime.datetime.now().year
        
    #-----------------------------------------------------------------------------------------