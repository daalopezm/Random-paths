from borracho import Borracho
class Campo:

    def __init__(self):
        self.coordenadas_de_borrachos = {}

    def anadir_borracho(self, borracho,coordenada):
        self.coordenadas_de_borrachos[borracho.nombre] = coordenada

    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borrachos[borracho.nombre]
        nueva_coordenada = coordenada_actual.mover(delta_x,delta_y)

        self.coordenadas_de_borrachos[borracho.nombre] = nueva_coordenada
    
    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho.nombre]
    
    def trazar_camino_borracho(self, borracho):
        borracho.camino.append(self.coordenadas_de_borrachos)
