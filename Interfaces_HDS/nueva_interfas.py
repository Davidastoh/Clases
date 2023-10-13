# # 1. importar TKinter --> Libreriria para la creacion de interfaz grafica
from tkinter import *
# # La libreriria tkinter tiene tres grandes clases para la creacion de interfaces 
# # Tk() --> Es la mas usada 
# # Tkk()  ---> tiene mas herramientas
# # Tcl()
# 2. Instanciar tk() como generar de interfaz grafica
nueva_ventana=Tk()
# 3. Frame tambien es una clase, Frame () para crear una frase que tengo que instanciar primero.
menu_principal=Frame()
# Montamos o inicializamos el frame
menu_principal.pack()
# Haciendo uso delmetodo config le damos un tamaño
menu_principal.config(width="200",height="200")
# Haciendo uso delmetodo config le asignamos un color
menu_principal.config(bg="blue")
# Metodo de Tk() que mantiene la ejecucion del programa en un boucle
nueva_ventana.mainloop()


