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