import matrices
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

    if opcion.lower() == "a": matriz = matrices.generarMatrizAleatoria(valorIngresado)
    else: matriz = matrices.generarMatrizManaulmente(valorIngresado)

    print("Matriz generada:")
    print(matriz)
    
    grafos.generarGrafo(matriz)

if __name__ == "__main__":
    main()