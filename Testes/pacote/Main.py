#!/usr/bin/python
# -*- coding: latin1 -*-

'''
Created on Oct 5, 2016

@author: tca85
'''

# Para importar a classe � melhor utilizar os atalhos do Eclipse,
# mas tamb�m segue o seguinte padr�o: 
# from pacote + nome do arquivo import NomeClasse
from pacote.Teste import Teste
from pacote.Arquivo import Arquivo

teste = Teste()

lista = teste.multiplicar_range_por_dois(15)

teste.testar_resto_igual_zero(lista, 3)

teste.tamanho_palavra('lsdfjfkjsdfkjas')

print teste.media(lista)
print teste.nome_sistema_operacional()

#-----------------------------------------------------------------------------
arquivo = Arquivo()

arquivo.criarArquivoTextoeEscrever('teste')
arquivo.mostrarListaArquivoTamanho()
arquivo.criarArquivoTemporario()
arquivo.gravarTextoArquivoCompactado()





