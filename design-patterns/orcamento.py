# -*- coding: UTF-8 -*-

'''
Created on Oct 17, 2016

https://cursos.alura.com.br/course/design-patterns-python
Design Patterns Python I: Boas práticas de programação

@author: tca85
'''

#=============================================================================================
class Orcamento(object):
    
    #-----------------------------------------------------------------------------------------
    '''
     Constructor
    '''
    def __init__(self, valor):    
        # atributo 'privado'
        self.__valor = valor
    
    #-----------------------------------------------------------------------------------------
    '''
     Criamos o atributo valor como property , mas com acesso de apenas leitura. Isso garante 
     que o valor recebido pelo construtor não seja alterado depois do orçamento criado
    '''
    @property
    def valor(self):
        return self.__valor
    
    #-----------------------------------------------------------------------------------------
#=============================================================================================