from tkinter import *
ventana=Tk()
ventana.geometry("300x350")
ventana.title("mi ventana")
def captura_dato():
    Text=text_nombre.get()
    mensaje=Label(ventana,text=f"hola,{Text}")
    mensaje.pack()
etiqueta=Label(ventana,text="Introduce tu nombre")
etiqueta.pack()
text_nombre=Entry(ventana)
text_nombre.config(bg="Blue",fg="white")
text_nombre.pack()

boton_capturar=Button(ventana,text="enviar",command=captura_dato)
boton_capturar.pack()
ventana.mainloop()

