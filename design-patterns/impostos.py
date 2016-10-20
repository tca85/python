# -*- coding: UTF-8 -*-

'''
Created on Oct 17, 2016

Todas classes que querem ser um imposto precisam ter o método calcula
(praticamente uma interface, não?)

@author: tca85
'''

from abc import ABCMeta, abstractmethod

#=============================================================================================
'''
 Poderíamos escrever um algoritmo que generaliza os outros dois, algo como um "molde":
'''
class Template_de_imposto_condicional(object):
    
    # atributo que define que essa é uma classe abstrata
    __metaclass__ = ABCMeta
    
    #-----------------------------------------------------------------------------------------
    def calcula(self, orcamento):
        
        # Bastaria agora fazer com que os impostos ICPP e IKCV possuam suas 
        # próprias implementações de deve_usar_maxima_taxacao, maxima_taxacao e minima_taxacao
        # ou seja, esses métodos são "buracos" e devem ser implementados por classes-filhas
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    #-----------------------------------------------------------------------------------------
    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento): pass
    #-----------------------------------------------------------------------------------------
    @abstractmethod
    def maxima_taxacao(self, orcamento): pass    
    #-----------------------------------------------------------------------------------------
    @abstractmethod
    def minima_taxacao(self, orcamento): pass    
    #-----------------------------------------------------------------------------------------

#=============================================================================================
class ICMS(object):
    
    #-----------------------------------------------------------------------------------------
    def calcula(self, orcamento):
        return orcamento.valor * 0.1
    #-----------------------------------------------------------------------------------------

#=============================================================================================
class ISS(object):
    
    #-----------------------------------------------------------------------------------------
    def calcula(self, orcamento):
        return orcamento.valor * 0.06
    #-----------------------------------------------------------------------------------------
#=============================================================================================

'''
  Veja que os dois impostos, apesar de diferentes, possuem uma estrutura em comum:
  Ambos checam o orçamento para ver se devem cobrar a taxação máxima e, a partir daí, 
  cobram a máxima ou a mínima.
  
  Regras parecidas podem vim de um 'molde', certo? Por isso criamos a classe abstrata
  Template_de_imposto_condicional, e fazemos ICPP e IKCV herdarem dela.
  
  Precisamos implementar todos métodos abstratos nas classes filhas, ou seja,
  deve_usar_maxima_taxacao, maxima_taxacao e minima_taxacao
  Outro detalhe importante: a assinatura tem que ser igual ao da classe pai, Template_de_imposto_condicional
  
  O método calcula é implementado na classe-pai, e não precisa ser re-escrito.
  
'''

class ICPP(Template_de_imposto_condicional):
    '''
     Implementação dos métodos abstratos herdados da classe pai
    '''
    #-----------------------------------------------------------------------------------------
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500
    #-----------------------------------------------------------------------------------------
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07
    #-----------------------------------------------------------------------------------------
    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05
    #-----------------------------------------------------------------------------------------
    
#=============================================================================================


class IKCV(Template_de_imposto_condicional):
    '''
     Implementação dos métodos abstratos herdados da classe pai
    '''
    #-----------------------------------------------------------------------------------------
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)
    #-----------------------------------------------------------------------------------------
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.10
    #-----------------------------------------------------------------------------------------
    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06
    #-----------------------------------------------------------------------------------------
    
    #-----------------------------------------------------------------------------------------
    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
            
            return False
    #-----------------------------------------------------------------------------------------

#=============================================================================================