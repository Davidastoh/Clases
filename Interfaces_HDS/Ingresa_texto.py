## Ingresar un cuadro de texto

# from tkinter import *
# ventana=Tk()
# ventana.geometry=("400x500")
# widget_uno=Frame()
# widget_uno.grid(row=0, column=0)
# widget_uno.config(width=400, height=100)
# etiqueta=Label(ventana,text="Ingrese su nombre")
# etiqueta.grid(row=1,column=0)
# cuadro_texto=Entry()
# cuadro_texto.grid(row=2, column=0)

# # usar el metodo mainloop para que la ventana permanezca abierta
# ventana=mainloop()

## Ingresar un cuadro de texto

from tkinter import *
ventana=Tk()
ventana.geometry=("400x500")
widget_uno=Frame()
widget_uno.grid(row=0, column=0)
widget_uno.config(width=400, height=100)
etiqueta=Label(ventana,text="Ingrese su nombre")
etiqueta.grid(row=1,column=0)
cuadro_texto=Entry()
cuadro_texto.grid(row=2, column=0)
widget_dos=Frame()
widget_dos.grid(row=3, column=0)
widget_dos.config(width=400, height=300)
# usar el metodo mainloop para que la ventana permanezca abierta
ventana=mainloop()

