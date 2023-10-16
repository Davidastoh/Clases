# Ingresar un cuadro de texto

from tkinter import *
ventana=Tk()
ventana.geometry=("400x500")
widget_uno=Frame()
widget_uno.grid(row=0, column=0,columnspan=2)
widget_uno.config(width=400, height=10)
etiqueta=Label(ventana,text="Nombre y Apellidos: ")
etiqueta.grid(row=1,column=0)
cuadro_texto=Entry()
cuadro_texto.grid(row=1, column=1)

widget_dos=Frame()
widget_dos.grid(row=2, column=0,columnspan=2)
widget_dos.config(width=400, height=10)
etiqueta=Label(ventana,text="DNI: ")
etiqueta.grid(row=3,column=0)
cuadro_texto=Entry()
cuadro_texto.grid(row=3, column=1)

widget_tres=Frame()
widget_tres.grid(row=4, column=0,columnspan=2)
widget_tres.config(width=400, height=10)
etiqueta=Label(ventana,text="Numero de celular: ")
etiqueta.grid(row=5,column=0)
cuadro_texto=Entry()
cuadro_texto.grid(row=5, column=1)

widget_cuatro=Frame()
widget_cuatro.grid(row=6, column=0,columnspan=2)
widget_cuatro.config(width=200, height=20)

widget_cinco=Frame()
widget_cinco.grid(row=7,column=0,columnspan=2)
widget_cinco.config(width="350",height="150")
widget_cinco.config(bg="blue")

widget_siete=Frame()
widget_siete.grid(row=8, column=0,columnspan=2)
widget_siete.config(width=200, height=20)

# usar el metodo mainloop para que la ventana permanezca abierta
ventana=mainloop()
