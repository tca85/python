# -*- coding: UTF-8 -*-

'''
Created on Oct 17, 2016

Todas classes que querem ser um imposto precisam ter o método calcula
(praticamente uma interface, não?)

@author: tca85
'''

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
 O imposto ICPP é calculado da seguinte forma: caso o valor do orçamento seja 
 menor que R$ 500,00, deve-se cobrar 5%; caso contrário, 7%.
'''
class ICPP(object):
    
    #-----------------------------------------------------------------------------------------
    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return orcamento.valor * 0.05
    #-----------------------------------------------------------------------------------------
    
#=============================================================================================

'''
 Já o imposto IKCV, caso o valor do orçamento seja maior que R$ 500,00 e algum item tiver valor
 superior a R$ 100,00, o imposto a ser cobrado é de 10%; caso contrário, 6%.
'''
class IKCV(object):
    
    #-----------------------------------------------------------------------------------------
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