from tkinter import *
ventana=Tk()
ventana.geometry("500x350")
ventana.title("Calculadora")

# # Suma
# a = 5
# b = 3
# resultado_suma = a + b
# print(resultado_suma)  # Salida: 8

# # Resta
# c = 10
# d = 7
# resultado_resta = c - d
# print(resultado_resta)  # Salida: 3

widget_uno=Frame()
widget_uno.grid(row=0, column=0,columnspan=4)
widget_uno.config(width=10, height=10)

etiqueta=Label(ventana,text="Ingrese un numero")
etiqueta.pack()
etiqueta.grid(row=1,column=1)

text_numero=Entry(ventana)
text_numero.config(bg="white",fg="Black")
text_numero.grid(row=2, column=1)

text_numero.pack()


# etiqueta=Label(ventana,text="Ingrese un numero")
# etiqueta.pack()
# text_usuario=Entry(ventana)
# text_usuario.config(bg="white",fg="Black")
# text_usuario.pack()

# etiqueta=Label(ventana,text="Total")
# etiqueta.pack()
# text_usuario=Entry(ventana)
# text_usuario.config(bg="white",fg="Black")
# text_usuario.pack()



# radioSumar=Radiobutton(ventana,text="Sumar",value=1,variable=info)
# radioMasculino.pack()

# radioRestar=Radiobutton(ventana,text="Restar",value=0,variable=info)
# radioFemenino.pack()

# boton_calcular=Button(ventana,text="Calcular",command=Calcular)
# boton_calcular.pack()

ventana.mainloop()