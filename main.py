import tkinter as tk
import matrices
import grafos
import dijkstra
from ventana import centrarVentana

matriz = None

def generar_matriz_aleatoria():
    global matriz
    n = int(n_entry.get())
    matriz = matrices.generarMatrizAleatoria(n)
    matriz_text.delete('1.0', tk.END)
    matriz_text.insert(tk.END, str(matriz))

def ingresar_matriz_manual():
    global matriz
    n = int(n_entry.get())
    entries = []
    ventanaMatriz = tk.Toplevel(app)
    ventanaMatriz.title("Ingrese la Matriz")

    for i in range(n):
        fila_entries = []
        for j in range(n):
            entry = tk.Entry(ventanaMatriz, width=5)
            entry.grid(row=i, column=j, padx=5, pady=5)
            fila_entries.append(entry)
        entries.append(fila_entries)

    def confirmar():
        matriz = [[int(entries[i][j].get()) for j in range(n)] for i in range(n)]
        matriz_text.delete('1.0', tk.END)
        matriz_text.insert(tk.END, str(matriz))
        ventanaMatriz.destroy()

    btn_confirmar = tk.Button(ventanaMatriz, text="Confirmar", command=confirmar)
    btn_confirmar.grid(row=n, columnspan=n)

    centrarVentana(ventanaMatriz)

def calcular_ruta():
    global matriz
    n = int(n_entry.get())
    if not 5 <= n <= 15:
        result_var.set("Número n inválido.")
        return

    matriz = matrices.generarMatrizAleatoria(n) if matrix_var.get() == "Aleatoria" else matrices.generarMatrizManualmente(n)
    matriz_text.delete('1.0', tk.END)
    matriz_text.insert(tk.END, str(matriz))

    inicio = int(inicio_entry.get()) - 1
    fin = int(fin_entry.get()) - 1

    ruta = dijkstra.mostrar(matriz, inicio, fin)
    result_var.set(f"La ruta más corta entre {inicio + 1} y {fin + 1} es: {ruta}")

def generarGrafoCamino():
    global matriz
    grafos.generarGrafo(matriz)

app = tk.Tk()
app.title("Menu proyecto")

tk.Label(app, text="Ingrese el valor de n(5-15):").pack(pady=10)
n_entry = tk.Entry(app)
n_entry.pack(pady=25, padx=200)

matrix_var = tk.StringVar(app)
matrix_var.set("Aleatoria")
tk.Label(app, text="Elija tipo de matriz:").pack(pady=10)

tk.Button(app, text="Generar matriz aleatoria", command=generar_matriz_aleatoria).pack(pady=10)
tk.Button(app, text="Generar matriz manual", command=ingresar_matriz_manual).pack(pady=10)
matriz_text = tk.Text(app, height=10, width=50)
matriz_text.pack(pady=20)

tk.Button(app, text="Generar grafo", command=generarGrafoCamino).pack(pady=20)

tk.Label(app, text="Ingrese el nodo de inicio:").pack(pady=10)
inicio_entry = tk.Entry(app)
inicio_entry.pack(pady=10)

tk.Label(app, text="Ingrese el nodo de fin:").pack(pady=10)
fin_entry = tk.Entry(app)
fin_entry.pack(pady=10)

tk.Button(app, text="Calcular ruta mas corta", command=calcular_ruta).pack(pady=20)

result_var = tk.StringVar(app)
result_var.set("La ruta aparecera aqui")
tk.Label(app, textvariable=result_var).pack(pady=10)

centrarVentana(app)
app.mainloop()
