from tkinter import *
ventana=Tk()
# ventana_litle("mi ventana")
ventana.geometry=("400x500")

header=Frame()
header.grid(row=0, column=1,columnspan=4)
header.config(width=500,height=10,bg="red")

# aside_left=Frame()
# aside_left.grid(row=1, column=0,columnspan=7)
# aside_left.config(width=15,height=385,bg="red")

etiqueta=Label(ventana,text="Usuario").grid(row=1,column=1)
text_usuario=Entry(ventana).grid(row=1,column=2)

section_uno=Frame()
section_uno.grid(row=2, column=1,columnspan=2)
section_uno.config(height=2,bg="red")

etiqueta=Label(ventana,text="Password").grid(row=3,column=1)
text_Password=Entry(ventana,show="*").grid(row=3,column=2)





# padx y pady



# column_izquierda.config(width=200, height=100)
# etiqueta=Label(ventana,text="Esta es mi etiqueta")
# etiqueta.grid(row=0,column=1)

# column_izquierda=Frame()
# column_izquierda.grid(row=2, column=0,columnspan=2)
# column_izquierda.config(width=200, height=100)
# etiqueta=Label(ventana,text="Esta es mi etiqueta")
# etiqueta.grid(row=0,column=1)

ventana=mainloop()

