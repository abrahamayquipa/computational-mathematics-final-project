def caminoMinimo(matriz, inicio, destino):
    n = len(matriz)
    distancias = [float("inf")] * n
    prev = [-1] * n
    distancias[inicio] = 0
    verticesNoVisitados = list(range(n))
    
    while verticesNoVisitados:
        verticeActual = min(verticesNoVisitados, key=lambda vertice: distancias[vertice])
        verticesNoVisitados.remove(verticeActual)
        
        for vertice, peso in enumerate(matriz[verticeActual]):
            rutaCandidata = distancias[verticeActual] + peso
            if rutaCandidata < distancias[vertice]:
                distancias[vertice] = rutaCandidata
                prev[vertice] = verticeActual

    camino = []
    while destino != -1:
        camino.insert(0, destino)
        destino = prev[destino]
        
    return camino