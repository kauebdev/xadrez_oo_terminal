# fazer um xadrez que rode em terminal, utilizando POO
 
from abc import ABC, abstractmethod
from typing import Type
 
"""
Peça
atributos:
nome - para identifação
posição - para poder saber em que lugar do tabuleiro esta e quais são os possiveis moviemntos
life - para saber se esta viva ou não
movimentos - movimentos da peça 
movimento_ataque - movimentos de ataque da peça
metodos populares{nao muda de peça para peça}:
Morrer() - se for morto por alguem 

metodos abstratos:
Movimentar() - checa seus movimentos e ve possiveis movimentos, e movimenta nos movimentos disponiveis
Matar() - checa seus movimentos de atque possiveis se a alguem por perto com base na sua posição e movimento e mata




-PEÇAS:         peão, torre, cavalo, bispo, rainha, rei
--MOVIMENTOS:   ↑ ↓ ← → ↖ ↗ ↙ ↘ ↰ ↱ ↳ ↲
_____________
-peão:          ↑ *come: ↖ ↗ - se for 1 vez pode andar dois
-torre:         ↑ ↓ ← → *come: ↑ ↓ ← → 
-cavalo:        ↰ ↱ ↳ ↲ *come: ↰ ↱ ↳ ↲ 
-bispo:         ↖ ↗ ↙ ↘ *come: ↖ ↗ ↙ ↘
-rainha:        ↑ ↓ ← → ↖ ↗ ↙ ↘ *come: ↑ ↓ ← → ↖ ↗ ↙ ↘
-rei:           ↑ ↓ ← → ↖ ↗ ↙ ↘ *porem o range e limitado a 1
"""
 
class peça(ABC):
    # construct
    def __init__(self, nome: type[str], initial_position: type[str]):
        self.__position = initial_position
        self.__nome = nome
        self.__life = True
        self.__movimentos = None
        self.__movimentos_ataque = None
 
    #Setters
    def SetPosition(self, new_position: type[str]):
        self.__position = new_position
 
    def SetNome(self, new_nome: type[str]):
        self.__nome = new_nome
 
    def SetLife(self, life: type[bool]):
        self.__life = life
 
    def SetMovimentos(self, movimentos: type[list]):
        self.__movimentos = movimentos
    
    def SetMovimentosAtaque(self, movimentos: type[list]):
        self.__movimentos_ataque = movimentos
 
    #Getters
    def GetPosition(self):
        return self.__position
 
    def GetNome(self):
        return self.__nome
 
    def GetLife(self):
        return self.__life
 
    def GetMovimentos(self):
        return self.__movimentos
    
    def GetMovimentosAtaque(self):
        return self.__movimentos_ataque
   
    # metodos populares
    def Morrer(self):
        if self.GetLife():
            self.SetLife = False
        return 'log: peça ja morta'
   
    # metodos abstratos
    @abstractmethod
    def Movimentar(self):
        pass

    def Matar(self):
        pass
    