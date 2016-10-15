# -*- coding: UTF-8 -*-

'''
Created on Oct 15, 2016

@author: tca85
'''

from models.Data import Data
from models.Perfil import Perfil
from models.Pessoa import Pessoa


perfil1 = Perfil('Thiago Cordeiro Alves', '+1 647 455 xxxx', 'SAP Labs Toronto')
perfil1.imprimir()

# também funciona referenciando em outra variável
outro = perfil1
print outro.nome

perfil1.curtir()
perfil1.curtir()
perfil1.curtir()
print perfil1.obter_curtidas()

# também é possível utilizar parâmetros nomeados
perfil2 = Perfil(empresa='Aché Laboratórios Farmacêuticos', telefone='xxx xxx xxxx', nome='Thiago em 2015')

# a função type e a propriedade class retornam agora um mesmo valor, o nome da classe
# essa é uma das diferenças entre o old style e o new style
print type(perfil2)
print perfil2.__class__

d = Data(21, 11, 2007)
d.imprime()

pessoa = Pessoa("Ronaldo", 105, 1.78)
pessoa.imprime_imc() 