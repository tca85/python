#!/usr/bin/python
# -*- coding: latin1 -*-

'''
Created on Oct 7, 2016

Essa classe cont�m meus primeiros c�digos feitos com Python
Vai ser utilizada somente para guardar c�digos aleat�rios
como testes da sintaxe, recursos, etc.

@author: tca85
'''

class Teste():

    #-----------------------------------------------------------------------------------------
    def multiplicar_range_por_dois(self, numero):
        """
        Retorna uma lista de numeros multiplicados por 2
        """
        lista = []
        num = 0
        
        for item in range(1, numero + 1):
            num = item * 2
            lista.append(num)
            
        return lista

    #-----------------------------------------------------------------------------------------
    def testar_resto_igual_zero(self, numero, divisor):
        for i in numero:
            if i % divisor == 0:
                print(i, '/3 = ', i / divisor)
            else:
                print(i, 'nao resta zero na divisao')
                
    #-----------------------------------------------------------------------------------------
    def somar_0_a_99(self):
        s = 0
        x = 1
        
        while x < 100:
            s = s + x
            x = x + 1
        
        print s

    #-----------------------------------------------------------------------------------------
    def fatorial(self, n):
        n = n if n > 1 else 1
        j = 1
        
        for i in range(1, n + 1):
            j = j * i
            return j
        
        
    #-----------------------------------------------------------------------------------------