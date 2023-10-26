import tkinter as interface
import matrices
import grafos
import dijkstra
from ventana import centrarVentana

#incicializar matriz en "None"
matriz = None

# Bibliografia:
# https://stackoverflow.com/questions/61661178/how-to-use-join-in-python

def formatoMatriz(matrix):
    # Tabulaciones y saltos de lineas para imprimir la matriz
    return '\n'.join(['\t'.join(map(str, row)) for row in matrix])

def generarMatrizAleatoria():
    global matriz
    n = int(valorIngresado.get())
    matriz = matrices.generadorMatrizAleatoria(n)
    # Lipiar matriz para setear valores
    matrizTexto.delete('1.0', interface.END)
    # insertar matriz
    matrizTexto.insert(interface.END, formatoMatriz(matriz))

def generarMatrizManual():
    n = int(valorIngresado.get())
    # Inicializacion de arreglo vacio
    entradas = []
    # Crear ventana de matriz manual
    ventanaMatriz = interface.Toplevel(aplicacion)
    ventanaMatriz.title("Ingrese la Matriz")

    # Crear input de texto
    for i in range(n):
        filaEntradas = []
        for j in range(n):
            entradasIndividuales = interface.Entry(ventanaMatriz, width=5)
            entradasIndividuales.grid(row=i, column=j, padx=5, pady=5)
            filaEntradas.append(entradasIndividuales)
        entradas.append(filaEntradas)

    def confirmar():
        # Crear matriz para los inputs
        global matriz
        matriz = [[int(entradas[i][j].get()) for j in range(n)] for i in range(n)]
        matrizTexto.delete('1.0', interface.END)
        matrizTexto.insert(interface.END, formatoMatriz(matriz))
        # Cerrar ventana
        ventanaMatriz.destroy()

    botonConfirmar = interface.Button(ventanaMatriz, text="Confirmar", command=confirmar)
    botonConfirmar.grid(row=n, columnspan=n)

    centrarVentana(ventanaMatriz)

def generarGrafoCamino():
    grafos.generarGrafo(matriz)

def calcularCaminoMinimo():
    inicio = int(nodoInicio.get()) - 1
    fin = int(nodoFinal.get()) - 1
    ruta = dijkstra.mostrar(matriz, inicio, fin)
    resultadoRuta.set(ruta)

aplicacion = interface.Tk()
aplicacion.title("Menu proyecto")

interface.Label(aplicacion, text="Ingrese el valor de n(5-15):").pack(pady=10)
valorIngresado = interface.Entry(aplicacion)
valorIngresado.pack(pady=25, padx=200)

tipoMatriz = interface.StringVar(aplicacion)
tipoMatriz.set("Aleatoria")
interface.Label(aplicacion, text="Elija tipo de matriz:").pack(pady=10)

interface.Button(aplicacion, text="Generar matriz aleatoria", command=generarMatrizAleatoria).pack(pady=10)
interface.Button(aplicacion, text="Generar matriz manual", command=generarMatrizManual).pack(pady=10)
matrizTexto = interface.Text(aplicacion, height=10, width=50)
matrizTexto.pack(pady=20)

interface.Button(aplicacion, text="Generar grafo", command=generarGrafoCamino).pack(pady=20)

interface.Label(aplicacion, text="Ingrese el nodo de inicio:").pack(pady=10)
nodoInicio = interface.Entry(aplicacion)
nodoInicio.pack(pady=10)

interface.Label(aplicacion, text="Ingrese el nodo de fin:").pack(pady=10)
nodoFinal = interface.Entry(aplicacion)
nodoFinal.pack(pady=10)

interface.Button(aplicacion, text="Calcular ruta mas corta", command=calcularCaminoMinimo).pack(pady=20)

resultadoRuta = interface.StringVar(aplicacion)
resultadoRuta.set("La ruta aparecera aqui")
interface.Label(aplicacion, textvariable=resultadoRuta).pack(pady=10)

centrarVentana(aplicacion)
aplicacion.mainloop()