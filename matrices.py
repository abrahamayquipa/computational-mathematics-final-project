import numpy
import random

def generarMatrizAleatoria(n):
    # Crea la matriz segun sus dimensiones nxn
    matriz = numpy.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            valorAleatorio = random.randint(0, 4)
            matriz[i, j] = valorAleatorio
            matriz[j, i] = valorAleatorio
    return matriz

def generarMatrizManaulmente(n):
    matriz = numpy.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i <= j:
                valor = int(input(f"Ingrese el valor para la posición ({i + 1}, {j + 1}): "))
                matriz[i, j] = valor
                matriz[j, i] = valor
    return matriz
