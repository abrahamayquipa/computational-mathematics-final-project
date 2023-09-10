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