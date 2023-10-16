# Creacion de etiquetas
from tkinter import *
# Instanciar la clase tK()
ventana=Tk()
ventana.geometry=("400x300")
# creo mis dos widget de orden inferior con la clase Frame()
widget_uno=Frame()
widget_uno.grid(row=0, column=0)
widget_uno.config(width=400, height=300)
widget_uno.config(bg="blue")
# creacion de etiquetas 
etiqueta=Label(ventana,text="Ingrese su nombre")
etiqueta.grid(row="0",column="0")
# usar el metodo mainloop para que la ventana permanezca abierta
ventana=mainloop()





