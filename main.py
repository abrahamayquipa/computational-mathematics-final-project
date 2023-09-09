import numpy as np
import matplotlib.pyplot as plt

# Función para generar matriz simétrica
def generar_matriz_simetrica(n):
    matriz = np.random.randint(0, 5, size=(n, n))
    for i in range(n):
        for j in range(i+1, n):
            matriz[j, i] = matriz[i, j]
    return matriz

# Función para ingresar matriz manualmente
def ingresar_matriz(n):
    matriz = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            valor = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
            matriz[i, j] = valor
            matriz[j, i] = valor
    return matriz

# Algoritmo de Dijkstra para camino mínimo
def dijkstra(matriz, inicio, destino):
    n = len(matriz)
    distancias = [float("inf")] * n
    prev = [-1] * n
    distancias[inicio] = 0
    vertices_no_visitados = list(range(n))
    
    while vertices_no_visitados:
        vertice_actual = min(vertices_no_visitados, key=lambda vertice: distancias[vertice])
        vertices_no_visitados.remove(vertice_actual)
        
        for vertice, peso in enumerate(matriz[vertice_actual]):
            ruta_candidata = distancias[vertice_actual] + peso
            if ruta_candidata < distancias[vertice]:
                distancias[vertice] = ruta_candidata
                prev[vertice] = vertice_actual

    camino = []
    while destino != -1:
        camino.insert(0, destino)
        destino = prev[destino]
        
    return camino

# Función para mostrar grafo
def mostrar_grafo(matriz):
    n = len(matriz)
    
    fig, ax = plt.subplots()
    coords = [(np.cos(2 * np.pi * i / n), np.sin(2 * np.pi * i / n)) for i in range(n)]
    
    # Dibuja nodos
    for x, y in coords:
        ax.scatter(x, y, s=500)
        
    # Dibuja aristas y etiquetas
    for i in range(n):
        for j in range(i+1, n):
            if matriz[i, j]:
                x1, y1 = coords[i]
                x2, y2 = coords[j]
                ax.plot([x1, x2], [y1, y2], 'k-')
                

    # Nombre de nodos
    for i, (x, y) in enumerate(coords):
        ax.text(x, y, str(i+1), ha='center', va='center', color='white')
    
    plt.axis("off")
    plt.show()

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