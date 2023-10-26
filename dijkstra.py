import numpy as np

def calcularRuta(matriz, nodoInicial, nodoFinal):
    n = len(matriz)
    # Lista infinita de distancias
    listaDistancias = [np.inf] * n
    # Establecemos la distancia del nodo inicial en 0
    listaDistancias[nodoInicial] = 0
    listaNodosNoVisitados = list(range(n))
    # Almacena unicamente el nodo anterior
    procedencia = [-1] * n

    while listaNodosNoVisitados:
        # Encuentra el nodo con la distancia mínima entre los nodos no visitados
        nodoActual = min(listaNodosNoVisitados, key=lambda x: listaDistancias[x])
        
        if nodoActual == nodoFinal:
            break
        
        # El nodo actual nunca contara como nodo no visitado
        listaNodosNoVisitados.remove(nodoActual)
        
        # Recorrido de todos los vecinos del nodo actual y actualizacion de  la lista de distancias y precedencias si se encuentra un camino más corto
        # Enumerate devuelve el inidice en la matriz
        for vecino, peso in enumerate(matriz[nodoActual]):
            # si son nodos conexos y no fue visitado
            if peso > 0 and vecino in listaNodosNoVisitados:
                nuevaDistancia = listaDistancias[nodoActual] + peso
                if nuevaDistancia < listaDistancias[vecino]:
                    listaDistancias[vecino] = nuevaDistancia
                    procedencia[vecino] = nodoActual

    listaCaminoNodos = []
    listaCaminoPesos = []
    
    while nodoFinal != nodoInicial:
        # Insertar fin al inicio
        listaCaminoNodos.insert(0, nodoFinal)
        # Insertar peso de la arista de que lleva al nodo fin desde su nodo procedencia
        listaCaminoPesos.insert(0, matriz[procedencia[nodoFinal]][nodoFinal])
        # Actualizamos fin con el nodo procedencia
        nodoFinal = procedencia[nodoFinal]
    listaCaminoNodos.insert(0, nodoInicial)
    # No necesitamos eliminar el último peso, así que eliminamos esta línea
    return listaCaminoNodos, listaCaminoPesos

def mostrar(matriz, nodoIncial, nodoFinal):
    caminoNodos, caminoPesos = calcularRuta(matriz, nodoIncial, nodoFinal)
    listaResultados = []
    
    for i in range(len(caminoNodos)):
        listaResultados.append(f"NODO: {caminoNodos[i] + 1}")
        # siempre y cuando que la longitud de "caminoPesos" sea menor a i, entonces...
        if i < len(caminoPesos):
            listaResultados.append(f" - PESO: {int(caminoPesos[i])} -> ")
    
    # Join convierte la lista en una cadena
    return ''.join(listaResultados)
