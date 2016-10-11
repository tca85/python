#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 11, 2016

https://cursos.alura.com.br/course/introducao-ao-python
Curso Python I: Programando com a linguagem

@author: tca85
'''

#-----------------------------------------------------------------------------------------
def cadastrar(nomes):
    print 'Digite: o nome:'
    nome = raw_input()
    nomes.append(nome)
    
#-----------------------------------------------------------------------------------------
def listar(nomes):
    print 'Listando nomes'
    
    for nome in nomes:
        print nome
    
#-----------------------------------------------------------------------------------------
def menu():
    nomes = []
    escolha = ''
    
    while (escolha != '0'):
        print 'Digite: 1 para cadastrar, 0 para terminar'
        escolha = raw_input()
        
        if(escolha == '1'):
            cadastrar(nomes)
        
        if(escolha == '2'):
            listar(nomes)
            
#-----------------------------------------------------------------------------------------
menu()