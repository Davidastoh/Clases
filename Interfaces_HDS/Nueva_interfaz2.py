# Importamos Tkinter
from tkinter import *
#instanciar la clase tk()
ventana=Tk()
#creo mis dos widget de orden inferior con la clase Frame()
#inastanciando mi primer widget
widget_uno=Frame()
# usar metodo para mostrar el frame
widget_uno.grid(row="0",column="0")
widget_uno.config(width="200",height="300")
widget_uno.config(bg="red")
# el metodo grid recibe dos parmetros el numero de la fila y de la columna donde quiero ubicar mi widget 
#creacion del segundo widget 
widget_dos=Frame()
widget_dos.grid(row="2",column="0")
widget_dos.config(width="100",height="100")
widget_dos.config(bg="blue")
#usar el metodo loop para que la ventana permanezaca abierta 
ventana.mainloop()
