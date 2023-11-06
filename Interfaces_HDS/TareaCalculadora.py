import tkinter as tk

def button_click(numero):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, str(actual) + str(numero))

def button_limpiar():
    entrada.delete(0, tk.END)

def button_igual():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

ventana = tk.Tk()
ventana.title("Calculadora")

entrada = tk.Entry(ventana, width=20, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "+"
]

fila = 1
columna = 0

for boton in botones:
    if columna == 4:
        columna = 0
        fila += 1

    boton = tk.Button(ventana, text=boton, padx=20, pady=10, command=lambda boton=boton: button_click(boton))
    boton.grid(row=fila, column=columna, padx=5, pady=5)
    columna += 1

boton_igual = tk.Button(ventana, text="=", padx=20, pady=10, command=button_igual)
boton_igual.grid(row=fila, column=columna, padx=5, pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", padx=20, pady=10, command=button_limpiar)
boton_limpiar.grid(row=fila+1, column=0, columnspan=4, padx=2, pady=5)

ventana.mainloop()