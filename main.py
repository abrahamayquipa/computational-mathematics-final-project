import numpy as np
import matplotlib.pyplot as plt
import matriz
import caminos
import grafos

def main():
    n = int(input("Ingrese el valor de n (entre 5 y 15): "))
    if not 5 <= n <= 15:
        print("Valor de n fuera de rango.")
        return

    opcion = input("¿Desea generar la matriz aleatoriamente? (s/n): ")
    if opcion.lower() == 's':
        matriz = generar_matriz_simetrica(n)
    else:
        matriz = ingresar_matriz(n)
    print("Matriz generada:")
    print(matriz)
    
    v1 = int(input(f"Seleccione el primer vértice (entre 1 y {n}): ")) - 1
    v2 = int(input(f"Seleccione el segundo vértice (entre 1 y {n}): ")) - 1

    camino = dijkstra(matriz, v1, v2)
    print(f"El camino mínimo entre {v1+1} y {v2+1} es: {' -> '.join(map(str, [x+1 for x in camino]))}")

    mostrar_grafo(matriz)

if __name__ == "__main__":
    main()