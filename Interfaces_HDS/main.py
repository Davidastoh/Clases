## Ejemplo de uso de TKinter

import tkinter as tk

ventana = tk.Tk()
def saludar():
    label_saludo.config(text="¡Hola, David!")

ventana.title("Mi ventana")
ventana.geometry("400x400")

label_saludo = tk.Label(ventana, text="Presiona el boton para saludar")
label_saludo.pack()

boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
boton_saludar.pack()

ventana.mainloop()
