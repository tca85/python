#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 5, 2016

@author: tca85
'''

# Para importar a classe é melhor utilizar os atalhos do Eclipse,
# mas também segue o seguinte padrão: 
# from pacote + nome do arquivo import NomeClasse
from pacote.Teste import Teste
from pacote.Arquivo import Arquivo
from pacote.DateTime import DateTime
from pacote.Cadastro import Cadastro

teste = Teste()

lista = teste.multiplicar_range_por_dois(15)

teste.testar_resto_igual_zero(lista, 3)

teste.tamanho_palavra('lsdfjfkjsdfkjas')

print teste.media(lista)
print teste.nome_sistema_operacional()

teste.exemplo_interpolacao()

print teste.inverter_string('thiago')
print teste.exemplo_string_template()

teste.exemplo_argumentos('peso', 10, unidade='k')

#-----------------------------------------------------------------------------
arquivo = Arquivo()

arquivo.criarArquivoTextoeEscrever('teste')
arquivo.mostrarListaArquivoTamanho()
arquivo.criarArquivoTemporario()
arquivo.gravarTextoArquivoCompactado()


#-----------------------------------------------------------------------------
datetime = DateTime()
datetime.testaClasseDateTime()


#-----------------------------------------------------------------------------
nomes = []

cadastro = Cadastro()
cadastro.nome(nomes)

print nomes

print cadastro.verificarAnoNascimento()




