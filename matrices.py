import numpy as np
import random

def generadorMatrizAleatoria(n):
    # Crea la matriz segun sus dimensiones nxn con tipo de dato int
    matriz = np.zeros((n, n), dtype=int)

    for i in range(n):
        for j in range(i, n):
            valorAleatorio = random.randint(0, 10)
            matriz[i, j] = valorAleatorio
            matriz[j, i] = valorAleatorio
    return matriz