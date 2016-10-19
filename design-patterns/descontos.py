# -*- coding: UTF-8 -*-

'''
Created on Oct 18, 2016

@author: tca85
'''

#=============================================================================================
class Desconto_por_cinco_itens(object):

    #-----------------------------------------------------------------------------------------
    def __init__(self, proximo_desconto):
        self._proximo_desconto = proximo_desconto
    #-----------------------------------------------------------------------------------------
    def calcular(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            # se não segue a regra, o desconto é zero!
            return 0
    #-----------------------------------------------------------------------------------------
            
#=============================================================================================
class Desconto_por_mais_de_quinhentos_reais(object):
    
    #-----------------------------------------------------------------------------------------
    def __init__(self, proximo_desconto):
        self._proximo_desconto = proximo_desconto
    #-----------------------------------------------------------------------------------------
    def calcular(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            # se não segue a regra, o desconto é zero!
            return 0
    #-----------------------------------------------------------------------------------------

#=============================================================================================    