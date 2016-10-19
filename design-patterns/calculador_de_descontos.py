# -*- coding: UTF-8 -*-

'''
Created on Oct 18, 2016

@author: tca85
'''

#=============================================================================================
class Calculador_de_descontos(object):
    
    #-----------------------------------------------------------------------------------------
    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        
        elif orcamento.valor > 500:
            return orcamento.valor * 0.07
        
    #-----------------------------------------------------------------------------------------

#=============================================================================================

'''
 A chamada da função main está sendo feita aqui para evitar criar uma classe para testar
'''
    
if __name__ == '__main__':
    from orcamento import Orcamento, Item
    
    orcamento = Orcamento()
    
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))
    
    calculador_de_descontos = Calculador_de_descontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    print 'Desconto calculado : %s' % (desconto)

