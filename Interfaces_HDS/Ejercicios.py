from tkinter import *
ventana = Tk()
widget_uno=Frame()
widget_uno.grid(row="0",column="1")
widget_uno.config(width="50",height="50")
widget_uno.config(bg="green")

widget_dos=Frame()
widget_dos.grid(row="0",column="2")
widget_dos.config(width="50",height="50")
widget_dos.config(bg="yellow")

widget_tres=Frame()
widget_tres.grid(row="1",column="1")
widget_tres.config(width="50",height="50")
widget_tres.config(bg="orange")

widget_cuatro=Frame()
widget_cuatro.grid(row="1",column="2")
widget_cuatro.config(width="50",height="50")
widget_cuatro.config(bg="purple")

widget_cinco=Frame()
widget_cinco.grid(row="2",column="1",columnspan="4")
widget_cinco.config(width="100",height="50")
widget_cinco.config(bg="blue")

widget_seis=Frame()
widget_seis.grid(row="3",column="1",columnspan="4")
widget_seis.config(width="100",height="50")
widget_seis.config(bg="red")

# Creacion de etiquetas
etiqueta=Label(ventana,text="Hola soy yo")
etiqueta.grid(row="2",column="1",columnspan="4")



ventana.mainloop()
