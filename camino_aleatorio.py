from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

campo_global = Campo()

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
    
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_de_intentos, tipo_Borracho):
    borracho=tipo_Borracho(nombre='David')
    origen = Coordenada(0,0)
    distancias = []
    
    for _ in range(numero_de_intentos):        
        campo_global.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo_global, borracho,pasos)
        distancias.append(round(simulacion_caminata,1))
    
    return distancias

def graficar(x,y):
    grafica = figure(title='Camino Aleatorio',x_axis_label='x',y_axis_label='y')
    grafica.line(x,y,legend='Camino')

    show(grafica)

def main(distancias_de_caminata, numero_de_intentos, tipo_Borracho):
    distancia_media_por_caminata = []
    for pasos in distancias_de_caminata:
        distancias=simular_caminata(pasos, numero_de_intentos,tipo_Borracho)
        distancia_media = round(sum(distancias)/len(distancias),4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancia_media_por_caminata.append(distancia_media)
        print(f'{tipo_Borracho.__name__} caminata aleatoria de {pasos}')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Minima = {distancia_minima}')
    
    #graficar(campo_global.coordenadas_de_borrachos[tipo_Borracho] ,campo_global.coordenadas_de_borrachos[tipo_Borracho])
    print(tipo_Borracho.camino_del_borracho)

    

if __name__ == '__main__':
    distancias_de_caminata = [10] # , 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)


