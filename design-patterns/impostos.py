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
'''

class ICPP(object):
    
    #-----------------------------------------------------------------------------------------
    '''
     O imposto ICPP é calculado da seguinte forma: caso o valor do orçamento seja 
     menor que R$ 500,00, deve-se cobrar 5%; caso contrário, 7%.
    '''    
    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return orcamento.valor * 0.05
    #-----------------------------------------------------------------------------------------
    
#=============================================================================================


class IKCV(object):
    
    #-----------------------------------------------------------------------------------------
    '''
     Já o imposto IKCV, caso o valor do orçamento seja maior que R$ 500,00 e algum item tiver valor
     superior a R$ 100,00, o imposto a ser cobrado é de 10%; caso contrário, 6%.
    '''
    def calcula(self, orcamento):
        if orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento):
            return orcamento.valor * 0.10
        else:
            return orcamento.valor * 0.06
    #-----------------------------------------------------------------------------------------
    
    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
            
            return False
    #-----------------------------------------------------------------------------------------

#=============================================================================================