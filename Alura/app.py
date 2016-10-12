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
def alterar_nomes_solucao2(nomes):
    print 'Qual nome vc gostaria de alterar?'
    nome_a_alterar = raw_input()
        
    if(nome_a_alterar in nomes):
        posicao = nomes.index(nome_a_alterar)
        print 'Digite novo nome:'
        nome_novo = raw_input()
        nomes[posicao] = nome_novo
#-----------------------------------------------------------------------------------------
def procurar(nomes):
    print 'Digite nome a procurar:'
    nome_a_procurar = raw_input()

    if(nome_a_procurar in nomes):
        print 'O nome', nomes[nomes.index(nome_a_procurar)],  'está na posição', nomes.index(nome_a_procurar)


#-----------------------------------------------------------------------------------------
def menu():
    nomes = []
    escolha = ''
    
    while (escolha != '0'):
        print '\n1 - Cadastrar \n2 - Listar \n3 - Remover \n4 - Alterar \n5 - Procurar \n0 - Sair'
        escolha = raw_input()
        
        if(escolha == '1'):
            cadastrar(nomes)
        
        if(escolha == '2'):
            listar(nomes)
        
        if(escolha == '3'):
            remover(nomes)
            
        if(escolha == '4'):
            alterar(nomes)
            
        if(escolha == '5'):
            procurar(nomes)
            
#-----------------------------------------------------------------------------------------
menu()