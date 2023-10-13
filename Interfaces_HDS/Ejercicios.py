from tkinter import *
ventana = Tk()
widget_uno=Frame()
widget_uno.grid(row="0",column="0")
widget_uno.config(width="200",height="300")
widget_uno.config(bg="green")

widget_dos=Frame()
widget_dos.grid(row="2",column="0")
widget_dos.config(width="100",height="100")
widget_dos.config(bg="yellow")

widget_tres=Frame()
widget_tres.grid(row="4",column="0")
widget_tres.config(width="100",height="100")
widget_tres.config(bg="orange")

widget_cuatro=Frame()
widget_cuatro.grid(row="3",column="0")
widget_cuatro.config(width="100",height="100")
widget_cuatro.config(bg="purple")

widget_cinco=Frame()
widget_cinco.grid(row="3",column="0")
widget_cinco.config(width="100",height="100")
widget_cinco.config(bg="blue")

widget_seis=Frame()
widget_seis.grid(row="3",column="0")
widget_seis.config(width="100",height="100")
widget_seis.config(bg="red")

ventana.mainloop()








