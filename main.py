# fazer um xadrez que rode em terminal, utilizando POO
 
from abc import ABC, abstractmethod
 
"""
-PEÇAS:         peão, torre, cavalo, bispo, rainha, rei
--MOVIMENTOS:   ↑ ↓ ← → ↖ ↗ ↙ ↘ ↰ ↱ ↳ ↲
_____________
-peão:          ↑ *come: ↖ ↗
-torre:         ↑ ↓ ← →
-cavalo:        ↰ ↱ ↳ ↲
-bispo:         ↖ ↗ ↙ ↘
-rainha:        ↑ ↓ ← → ↖ ↗ ↙ ↘
-rei:           ↑ ↓ ← → ↖ ↗ ↙ ↘ *porem o range e limitado a 1
"""
 
class peça(ABC):
    # construct
    def __init__(self, nome, initial_position):
        self.position = initial_position
        self.nome = nome
        self.life = True
        self.movimentos = None
 
    #Setters
    def SetPosition(self, new_position):
        self.position = new_position
 
    def SetNome(self, new_nome):
        self.nome = new_nome
 
    def SetLife(self, life):
        self.life = life
 
    def SetMovimentos(self, movimentos):
        self.movimentos = movimentos
 
    #Getters
    def GetPosition(self):
        return self.position
 
    def GetNome(self):
        return self.nome
 
    def GetLife(self):
        return self.life
 
    def GetMovimentos(self):
        return self.movimentos
   
    # metodos populares
    def EliminarPeça(self):
        if self.GetLife():
            self.SetLife = False
        return 'log: peça ja morta'
   
    # metodos abstratos
    @abstractmethod
    def Movimentar(self):
        pass