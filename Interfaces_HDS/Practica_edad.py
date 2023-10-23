from tkinter import *
ventana=Tk()
ventana.geometry("300x400")
ventana.title("mi ventana")

def evaluar_edad():
    edad=int(text_edad.get())
    nombre=text_nombre.get()
    if edad < 18:
        mensaje=Label(ventana,text=f"Hola {nombre}, eres menor de edad")
        mensaje.config
    else:
        mensaje=Label(ventana,text=f"Hola {nombre}, eres mayor de edad")
    mensaje.pack()

def captura_dato():

    Text=text_nombre.get()
    mensaje=Label(ventana,text=f"hola,{Text}")
    mensaje.pack()

etiqueta=Label(ventana,text="Introduce tu nombre")
etiqueta.pack()
text_nombre=Entry(ventana)
text_nombre.config(bg="Blue",fg="white")
text_nombre.pack()

etiqueta=Label(ventana,text="Introduce tu edad")
etiqueta.pack()
text_edad=Entry(ventana)
text_edad.config(bg="Blue",fg="white")
text_edad.pack()

boton_evaluar=Button(ventana,text="Evaluar",command=evaluar_edad)
boton_evaluar.pack()



ventana.mainloop()