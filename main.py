import matrices
import caminos
import grafos

def main():
    print("\nMENU PROYECTO 2:")
    valorIngresado = int(input("Ingrese el valor de n(5-15): "))
    if not 5 <= valorIngresado <= 15:
        print("Número n invalido.")
        return

    print("a. Generar matriz aleatoria")
    print("b. Generar matriz manualmente")
    opcion = input("Ingresar opcion: ")
    if opcion.lower() == "a":
        matriz = matrices.generarMatrizAleatoria(valorIngresado)
    else:
        matriz = matrices.generarMatrizManaulmente(valorIngresado)
    print("Matriz generada:")
    print(matriz)
    
    primerVertice= int(input(f"Seleccione el primer vértice (entre 1 y {valorIngresado}): ")) - 1
    segundoVertice = int(input(f"Seleccione el segundo vértice (entre 1 y {valorIngresado}): ")) - 1

    camino = caminos.caminoMinimo(matriz, primerVertice, segundoVertice)
    print(f"El camino mínimo entre {primerVertice + 1} y {segundoVertice + 1} es:\n{' -> '.join(map(str, [x + 1 for x in camino]))}")

    grafos.generarGrafo(matriz)

if __name__ == "__main__":
    main()