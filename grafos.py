import numpy
import matplotlib.pyplot as matplot

# Función para mostrar grafo
def generarGrafo(matriz):
    n = len(matriz)
    
    coordenadaAleatoriaX = numpy.random.rand(n) * 5
    coordenadaAleatoriaY = numpy.random.rand(n) * 5
    coordenadas = list(zip(coordenadaAleatoriaX, coordenadaAleatoriaY))
    
    # Crear objeto
    fig, objeto = matplot.subplots()

    # Dibuja nodos con color gris
    for x, y in coordenadas:
        objeto.scatter(x, y, s=800, color='gray')
        
    # Dibuja aristas y etiquetas
    for i in range(n):
        for j in range(i+1, n):
            if matriz[i, j]:
                x1, y1 = coordenadas[i]
                x2, y2 = coordenadas[j]
                # k significa negro y - indica una línea continua.
                objeto.plot([x1, x2], [y1, y2], 'k-')

    # Nombre de nodos en letras blancas
    for i, (x, y) in enumerate(coordenadas):
        objeto.text(x, y, str(i + 1), ha='center', va='center', color='white')
    
    # Desactiva los ejes predeterminados
    matplot.axis("off")
    matplot.show()