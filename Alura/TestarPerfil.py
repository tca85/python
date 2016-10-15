# -*- coding: UTF-8 -*-

'''
Created on Oct 15, 2016

@author: tca85
'''

from models.Perfil import Perfil

perfil1 = Perfil('Thiago Cordeiro Alves', '+1 647 455 xxxx', 'SAP Labs Toronto')
perfil1.imprimir()

# também é possível utilizar parâmetros nomeados
perfil = Perfil(empresa='Aché Laboratórios Farmacêuticos', telefone='xxx xxx xxxx', nome='Thiago em 2015')

# a função type e a propriedade class retornam agora um mesmo valor, o nome da classe
# essa é uma das diferenças entre o old style e o new style
print type(perfil)
print perfil.__class__