import numpy as np
import matplotlib.pyplot as matplot
import random
from ventana import centrarVentana

# Función para mostrar grafo
def generarGrafo(matriz):
    # valor de n para la dimension de la matriz
    n = len(matriz)

    valorAleatorio = random.randint(1, 2)
    coordenadas = [(np.cos(2 * np.pi * i / n), np.sin(2 * np.pi * i / n)) for i in range(n)]

    # Crear objeto
    fig, objeto = matplot.subplots()

    # Dibuja nodos con color gris
    for x, y in coordenadas:
        objeto.scatter(x, y, s=800, color='gray')

    # Dibuja aristas y etiquetas
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i, j]:
                x1, y1 = coordenadas[i]
                x2, y2 = coordenadas[j]
                # k significa negro y - indica una línea continua.
                objeto.plot([x1, x2], [y1, y2], 'k-')
                # Calcula la posición media entre los dos puntos para la etiqueta
                valorAleatorio = random.randint(5, 20)
                posicionMediaEtiquetaX = x1 + (valorAleatorio / 25) * (x2 - x1)
                posicionMediaEtiquetaY = y1 + (valorAleatorio / 25) * (y2 - y1)
                valorEntero = int(matriz[i][j])
                # Imprime el valor de los caminos
                objeto.text(posicionMediaEtiquetaX, posicionMediaEtiquetaY, str(valorEntero), ha='center', va='center', color='black', bbox=dict(facecolor='white', edgecolor='white'))

    # Nombre de nodos en letras blancas
    for i, (x, y) in enumerate(coordenadas):
        objeto.text(x, y, str(i + 1), ha='center', va='center', color='white')
    
    # Desactiva los ejes predeterminados
    matplot.axis("off")

    # Centra la ventana de la figura antes de mostrarla
    manager = matplot.get_current_fig_manager()
    centrarVentana(manager.window)

    matplot.show()