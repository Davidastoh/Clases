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

etiqueta=Label(ventana,text="Ingrese un numero")
etiqueta.pack()
text_usuario=Entry(ventana)
text_usuario.config(bg="white",fg="Black")
text_usuario.pack()

etiqueta=Label(ventana,text="Ingrese un numero")
etiqueta.pack()
text_contraseña=Entry(ventana)
text_contraseña.config(bg="white",fg="Black")
text_contraseña.pack()

radioSuma=Radiobutton(ventana,text="Suma")
radioSuma.pack()

radioResta=Radiobutton(ventana,text="Resta")
radioResta.pack()

radioMultiplicacion=Radiobutton(ventana,text="Multiplicacion")
radioResta.pack()

radioDivision=Radiobutton(ventana,text="Division")
radioResta.pack()

# radioSumar=Radiobutton(ventana,text="Sumar",value=1,variable=info)
# radioMasculino.pack()

# radioRestar=Radiobutton(ventana,text="Restar",value=0,variable=info)
# radioFemenino.pack()

# boton_calcular=Button(ventana,text="Calcular",command=Calcular)
# boton_calcular.pack()

ventana.mainloop()