# -*- coding: UTF-8 -*-

'''
Created on Oct 18, 2016

@author: tca85
'''

from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

'''
 Precisamos de uma classe que monte essa corrente na ordem certa com todos os descontos necessários
 por isso a classe Calculador_de_descontos é essencial para a utilização desse design pattern
'''
#=============================================================================================
class Calculador_de_descontos(object):
    
    '''
      Faz o cálculo utilizando o design pattern Chain of Responsibility
    '''
    #-----------------------------------------------------------------------------------------
    def calcula(self, orcamento):
        return Desconto_por_cinco_itens(
                   Desconto_por_mais_de_quinhentos_reais(
                       Sem_desconto()
                   )
               ).calcular(orcamento)
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

