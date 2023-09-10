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