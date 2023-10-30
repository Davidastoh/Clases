import tkinter as tk

def calcular():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    
    if operacion.get() == 1:
        resultado = num1 + num2
    elif operacion.get() == 2:
        resultado = num1 - num2
    elif operacion.get() == 3:
        resultado = num1 * num2
    elif operacion.get() == 4:
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: División por cero"
    
    etiqueta_resultado.config(text="Resultado: " + str(resultado))

def limpiar():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    etiqueta_resultado.config(text="Resultado:")


ventana = tk.Tk()
ventana.geometry("400x350")
ventana.title("Calculadora")

etiqueta_num1 = tk.Label(ventana, text="Ingrese un numero")
etiqueta_num1.pack()

entry_num1 = tk.Entry(ventana)
entry_num1.pack()

etiqueta_num2 = tk.Label(ventana, text="Ingrese un numero")
etiqueta_num2.pack()

entry_num2 = tk.Entry(ventana)
entry_num2.pack()

operacion = tk.IntVar()

radio_sumar = tk.Radiobutton(ventana, text="Sumar", variable=operacion, value=1)
radio_sumar.pack()

radio_restar = tk.Radiobutton(ventana, text="Restar", variable=operacion, value=2)
radio_restar.pack()

radio_multiplicar = tk.Radiobutton(ventana, text="Multiplicar", variable=operacion, value=3)
radio_multiplicar.pack()

radio_dividir = tk.Radiobutton(ventana, text="Dividir", variable=operacion, value=4)
radio_dividir.pack()


boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack()

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack()

etiqueta_resultado = tk.Label(ventana, text="Resultado:")
etiqueta_resultado.pack()

ventana.mainloop()