# -*- coding: UTF-8 -*-

'''
Created on Oct 17, 2016

https://cursos.alura.com.br/course/design-patterns-python
Design Patterns Python I: Boas práticas de programação

@author: tca85
'''

#=============================================================================================
class Calculador_de_impostos(object):
    
    #-----------------------------------------------------------------------------------------
    '''
     Realiza cálculo
    '''
    def realiza_calculo(self, orcamento, imposto):
        
        if 'ICMS' == imposto:
            icms_calculado = orcamento.valor * 0.1
            print icms_calculado
            
        elif 'ISS' == imposto:
            iss_calculado = orcamento.valor * 0.06
            print iss_calculado
        
        
        icms_calculado = orcamento.valor * 0.1
        print icms_calculado
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
