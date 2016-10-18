# -*- coding: UTF-8 -*-

'''
Created on Oct 17, 2016

https://cursos.alura.com.br/course/design-patterns-python
Design Patterns Python I: Boas práticas de programação

@author: tca85
'''

from impostos import calcula_ISS, calcula_ICMS

#=============================================================================================
class Calculador_de_impostos(object):
    
    #-----------------------------------------------------------------------------------------
    '''
     Realiza cálculo
    '''
    def realiza_calculo(self, orcamento, imposto):
        
        # Essa não é a forma ideal porque se houver mais um imposto teremos que modificar o código
        # podemos melhorar um pouco modularizando o código fazendo a chamada de uma função
        # impostos.calcula_ICMS
        if 'ICMS' == imposto:
            icms_calculado = calcula_ICMS(orcamento.valor)
            print icms_calculado
            
        elif 'ISS' == imposto:
            iss_calculado = calcula_ISS(orcamento.valor)
            print iss_calculado
        
    #-----------------------------------------------------------------------------------------
#=============================================================================================    
    
'''
 A chamada da função main está sendo feita aqui para evitar criar uma classe para testar
'''
if __name__ == '__main__':
    from orcamento import Orcamento
      
    orcamento = Orcamento(500.0)
        
    calculador_de_impostos = Calculador_de_impostos()
    
    # Qual o imposto terá o cálculo realizado (hard-code)
    calculador_de_impostos.realiza_calculo(orcamento, 'ICMS')
    calculador_de_impostos.realiza_calculo(orcamento, 'ISS')
    
#-----------------------------------------------------------------------------------------
