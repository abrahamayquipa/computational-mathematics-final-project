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