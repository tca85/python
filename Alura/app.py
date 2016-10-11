#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 11, 2016

https://cursos.alura.com.br/course/introducao-ao-python
Curso Python I: Programando com a linguagem

@author: tca85
'''
from mercurial.templater import if_

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
def remover(nomes):
    print 'Qual nome você gostaria de remover?'
    nome = raw_input()
    
    if len(nome) != 0:
        nomes.remove(nome)

#-----------------------------------------------------------------------------------------
def alterar(nomes):
    print 'Qual nome você gostaria de alterar?'
    nome_inserido = raw_input()
    
    for indice, nome in enumerate(nomes):
        if nome == nome_inserido:
            print 'Informe o novo nome'
            nomes[indice] = raw_input()
        else:
            print 'Nome não encontrado'
    
        
#-----------------------------------------------------------------------------------------
def menu():
    nomes = []
    escolha = ''
    
    while (escolha != '0'):
        print '\n1 - Cadastrar \n2 - Listar \n3 - Remover \n4 - Alterar \n0 - Sair'
        escolha = raw_input()
        
        if(escolha == '1'):
            cadastrar(nomes)
        
        if(escolha == '2'):
            listar(nomes)
        
        if(escolha == '3'):
            remover(nomes)
            
        if(escolha == '4'):
            alterar(nomes)
            
#-----------------------------------------------------------------------------------------
menu()