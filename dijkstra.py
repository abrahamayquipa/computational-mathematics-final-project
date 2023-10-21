import numpy as np

def dijkstra(matriz, inicio, fin):
    n = len(matriz)
    distancias = [np.inf] * n
    distancias[inicio] = 0
    nodosNoVisitados = list(range(n))
    procedencia = [-1] * n

    while nodosNoVisitados:
        nodoActual = min(nodosNoVisitados, key=lambda x: distancias[x])
        
        if nodoActual == fin:
            break
        
        nodosNoVisitados.remove(nodoActual)
        
        for vecino, peso in enumerate(matriz[nodoActual]):
            if peso > 0 and vecino in nodosNoVisitados:
                nuevaDistancia = distancias[nodoActual] + peso
                if nuevaDistancia < distancias[vecino]:
                    distancias[vecino] = nuevaDistancia
                    procedencia[vecino] = nodoActual

    caminoNodos = []
    caminoPesos = []
    
    while fin != inicio:
        caminoNodos.insert(0, fin)
        caminoPesos.insert(0, matriz[procedencia[fin]][fin])
        fin = procedencia[fin]
    caminoNodos.insert(0, inicio)
    # No necesitamos eliminar el último peso, así que eliminamos esta línea
    return caminoNodos, caminoPesos

def mostrar(matriz, inicio, fin):
    caminoNodos, caminoPesos = dijkstra(matriz, inicio, fin)
    resultado = []
    
    for i in range(len(caminoNodos)):
        resultado.append(f"NODO: {caminoNodos[i] + 1}")
        if i < len(caminoPesos):
            resultado.append(f" - PESO: {int(caminoPesos[i])} -> ")
    
    # Join convierte la lista en una cadena
    return ''.join(resultado)
