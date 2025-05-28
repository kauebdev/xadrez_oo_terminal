# criação de cada peça

from peça import peça

class Peao(peça):
    def __init__(self, nome, initial_position):
        super().__init__(nome, initial_position)
        self.SetMovimentos(['UP'])

    def Movimentar(self):
        movimentos = self.GetMovimentos() 

