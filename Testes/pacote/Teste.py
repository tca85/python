#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 9, 2016

Essa classe contém meus primeiros códigos feitos com Python
Vai ser utilizada somente para guardar códigos aleatórios
como testes da sintaxe, recursos, etc.

@author: tca85
'''
import os
import string


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
                print(i, 'não resta zero na divisão')
                
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
    def tamanho_palavra(self, palavra):
        print 'Tamanho de %s = %d' % (palavra, len(palavra))
    
    #-----------------------------------------------------------------------------------------
    def media(self, lista):
        return float(sum(lista) / len(lista))
    
    
    #-----------------------------------------------------------------------------------------
    def nome_sistema_operacional(self):
        return os.name
    
    #-----------------------------------------------------------------------------------------
    def exemplo_interpolacao(self):
        musicos = [('Page', 'guitarrista', 'Led Zeppelin'),
                   ('Fripp', 'guitarrista', 'XPTO band')]
        
        msg = '{0} � {1} do {2}'
        
        for nome, funcao, banda in musicos:
            print(msg.format(nome, funcao, banda))
        
        msg = '{saudacao}, s�o {hora:02d}:{minuto:02d}'
        
        print msg.format(saudacao='Bom dia', hora=7, minuto=30)        
        
    #-----------------------------------------------------------------------------------------
    def inverter_string(self, texto):
        return texto[::-1]
    
    
    #-----------------------------------------------------------------------------------------
    def exemplo_string_template(self):
        # string template
        st = string.Template('$aviso aconteceu em $quando')
        
        return st.substitute({'aviso':'falta de eletricidade', 'quando':'02 de Outubro de 2016'})
        
        
    #-----------------------------------------------------------------------------------------
    def exemplo_listas_mutaveis(self):
        # Uma nova lista: Brit Progs dos anos 70
        progs = ['Yes', 'Genesis', 'Pink Floyd', 'ELP']

        # Varrendo a lista inteira
        for prog in progs:
            print prog

        # Trocando o �ltimo elemento
        progs[-1] = 'King Crimson'

        # Incluindo
        progs.append('Camel')

        # Removendo
        progs.remove('Pink Floyd')

        # Ordena a lista
        progs.sort()

        # Inverte a lista
        progs.reverse()

        # Imprime numerado
        for i, prog in enumerate(progs):
            print i + 1, '=>', prog

        # Imprime do segundo item em diante
        print progs[1:]
        
    
    #-----------------------------------------------------------------------------------------
    def exemplo_sequencias(self):
        # Conjuntos de dados
        # set: sequ�ncia mut�vel un�voca (sem repeti��es) n�o ordenada.
        # Quando uma lista � convertida para set, as repeti��es s�o descartadas.
        s1 = set(range(3))
        s2 = set(range(10, 7, -1))
        s3 = set(range(2, 10, 2))
        
        print 's1:', s1, '\ns2:', s2, '\ns3:', s3
        
        s1s2 = s1.union(s2)
        
        print 'Uni�o de s1 e s2:', s1s2
        print 'Diferen�a com s3:', s1s2.difference(s3)
        print 'Interse��o com s3:', s1s2.intersection(s3)
        
        if s1.issuperset([1, 2]):
            print 's1 inclui 1 e 2'
            
        if s1.isdisjoint(s2):
            print 's1 e s2 n�o tem elementos em comum'
        
    #-----------------------------------------------------------------------------------------
    def exemplo_dicionario(self):
        dic = {'nome': 'Shirley Manson', 'banda': 'Garbage'}
        
        print dic['nome']
        
        #adiconando elementos
        dic['album'] = 'Version 2.0'
        
        #apagando elemento
        del dic['album']
        
        itens = dic.items()
        chaves = dic.keys()
        valores = dic.values()
    
    #-----------------------------------------------------------------------------------------
    def exemplo_dicionario2(self):
        cds_metal = {'Metallica': ['Master of Puppets', 'Black'],
                     'Slayer': ['Season in the Abyss', 'Raining Blood'],
                     'Cannibal Corpse': ['Live Cannibalism', 'Butchered at Birth']}
        
        for cd, albuns in cds_metal.items():
            print cd, '=> ', albuns
        
        if cds_metal.has_key('Slayer'):
            del cds_metal['Slayer']
        
        
    #-----------------------------------------------------------------------------------------
    def exemplo_argumentos(self, *args, **kargs):
        # *args - argumentos sem nome (lista)
        # **kargs - argumentos com nome (dicion�rio)    
        print args
        print kargs
    
    