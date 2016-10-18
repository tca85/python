# -*- coding: UTF-8 -*-

'''
Created on Oct 17, 2016

https://cursos.alura.com.br/course/design-patterns-python
Design Patterns Python I: Boas práticas de programação

Design Pattern nada é que uma solução elegante para um problema 
que é muito recorrente em nosso dia-a-dia

@author: tca85
'''

#=============================================================================================
class Calculador_de_impostos(object):
    
    #-----------------------------------------------------------------------------------------
    '''
     Realiza cálculo
     
     Utiliza o Design Pattern "Strategy". Basicamente ele recebe qualquer classe que tenha
     o método "calcula()", como se fosse uma interface. Também é chamado de Duck Typing essa
     estratégia de receber "qualquer coisa" que tenha o método desejado
     
    '''
    def realiza_calculo(self, orcamento, imposto):
        print imposto.calcula(orcamento)
               
    #-----------------------------------------------------------------------------------------
#=============================================================================================    
    
'''
 A chamada da função main está sendo feita aqui para evitar criar uma classe para testar
'''
if __name__ == '__main__':
    from orcamento import Orcamento
    from impostos import ICMS, ISS
      
    orcamento = Orcamento(500.0)
        
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())
    
#-----------------------------------------------------------------------------------------
