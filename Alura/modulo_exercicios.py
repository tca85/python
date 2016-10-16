# -*- coding: UTF-8 -*-

'''
Created on Oct 15, 2016

Curso Python I: Programando com a linguagem
https://cursos.alura.com.br/course/introducao-ao-python
Python 2.7

@author: tca85
'''

class Pessoa(object):

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        
    def imprime_imc(self):
        peso = float(self.peso)
        altura = float(self.altura)
        
        imc = peso / (altura ** 2)
        
        print 'Imc de %s : %f' % (self.nome, imc)
        
class Data(object):

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def imprime(self):
        print '%s/%s/%s' % (self.dia, self.mes, self.ano)
        