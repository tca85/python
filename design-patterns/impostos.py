# -*- coding: UTF-8 -*-

'''
Created on Oct 17, 2016

Todas classes que querem ser um imposto precisam ter o método calcula
(praticamente uma interface, não?)

@author: tca85
'''

from abc import ABCMeta, abstractmethod

#=============================================================================================
'''
 Repare que no padrão Template method a classe mãe controla os filhos. Os filhos preenchem apenas 
 as lacunas da mãe, aquele métodos abstratos, mas a classe mãe está no poder e chama estes métodos dos filhos.
 
 Esse fato que filhos não ficam mais no controle da execução também é chamado de 
 The Hollywood Principle. Esse princípio diz: “Don't call us, we'll call you”! Ou seja, invés você 
 (os filhos) ficarem chamando a classe pai, o controle é invertido e a classe mãe chama os filhos.

 A ideia de inverter o controle (IoC - Inversion of Control) vai muito mais longe e 
 não é usado apenas no Template Method
'''
class Template_de_imposto_condicional(object):
    
    # atributo que define que essa é uma classe abstrata
    __metaclass__ = ABCMeta
    
    #-----------------------------------------------------------------------------------------
    def calcula(self, orcamento):
        
        # Bastaria agora fazer com que os impostos ICPP e IKCV possuam suas 
        # próprias implementações de deve_usar_maxima_taxacao, maxima_taxacao e minima_taxacao
        # ou seja, esses métodos são "buracos" e devem ser implementados por classes-filhas
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    '''
     Como o método abstrato nada faz e aguarda sua implementação por uma classe filha, precisamos 
     colocar a instrução pass, porque Python não suporta a criação de métodos ou funções que nada fazem, 
     uma instrução no mínimo é requerida.
    '''
    #-----------------------------------------------------------------------------------------
    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento): pass
    #-----------------------------------------------------------------------------------------
    @abstractmethod
    def maxima_taxacao(self, orcamento): pass    
    #-----------------------------------------------------------------------------------------
    @abstractmethod
    def minima_taxacao(self, orcamento): pass    
    #-----------------------------------------------------------------------------------------

#=============================================================================================
class ICMS(object):
    
    #-----------------------------------------------------------------------------------------
    def calcula(self, orcamento):
        return orcamento.valor * 0.1
    #-----------------------------------------------------------------------------------------

#=============================================================================================
class ISS(object):
    
    #-----------------------------------------------------------------------------------------
    def calcula(self, orcamento):
        return orcamento.valor * 0.06
    #-----------------------------------------------------------------------------------------
#=============================================================================================

'''
  Veja que os dois impostos, apesar de diferentes, possuem uma estrutura em comum:
  Ambos checam o orçamento para ver se devem cobrar a taxação máxima e, a partir daí, 
  cobram a máxima ou a mínima.
  
  Regras parecidas podem vim de um 'molde', certo? Por isso criamos a classe abstrata
  Template_de_imposto_condicional, e fazemos ICPP e IKCV herdarem dela.
  
  O método calcula é implementado na classe-pai, e não precisa ser re-escrito.
  
  Perceba que ambas as classes de impostos só implementam as partes "que faltam" do algoritmo.
  A classe Template_de_imposto_condicional possui um método que funciona como um template, 
  ou seja, um molde, para as classes filhas. Daí o nome do padrão de projeto: Template Method.
'''

class ICPP(Template_de_imposto_condicional):
    '''
     Implementação dos métodos abstratos herdados da classe pai
    '''
    #-----------------------------------------------------------------------------------------
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500
    #-----------------------------------------------------------------------------------------
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07
    #-----------------------------------------------------------------------------------------
    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05
    #-----------------------------------------------------------------------------------------
    
#=============================================================================================


class IKCV(Template_de_imposto_condicional):
    '''
     Implementação dos métodos abstratos herdados da classe pai
    '''
    #-----------------------------------------------------------------------------------------
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)
    #-----------------------------------------------------------------------------------------
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.10
    #-----------------------------------------------------------------------------------------
    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06
    #-----------------------------------------------------------------------------------------
    
    #-----------------------------------------------------------------------------------------
    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
            
            return False
    #-----------------------------------------------------------------------------------------

#=============================================================================================