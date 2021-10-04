import random

class Borracho:

    def __init__(self,nombre):
        self.nombre = nombre
        self.camino = []

class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])

    def camino_del_borracho(self,coordenada):

        return self.camino

    
