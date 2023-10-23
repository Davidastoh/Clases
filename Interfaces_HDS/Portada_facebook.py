from tkinter import *
ventana=Tk()
ventana.geometry("300x350")
ventana.title("mi ventana")

Usuario="David"
Contraseña="1234"

def evaluar_datos():
    Usuario_text=text_usuario.get()
    Contraseña_text=text_contraseña.get()
    
    if Usuario_text==Usuario and Contraseña_text==Contraseña:
        mensaje=Label(ventana,text=f"Hola {Usuario}, Bienvenido a Facebook")
        mensaje.pack()
    else:
        mensaje=Label(ventana,text=f"Los datos no coinciden")
        mensaje.pack()

def captura_dato():

    Text=text_usuario.get()
    mensaje=Label(ventana,text=f"hola,{Text}")
    mensaje.pack()


etiqueta=Label(ventana,text="Usuario")
etiqueta.pack()
text_usuario=Entry(ventana)
text_usuario.config(bg="Blue",fg="white")
text_usuario.pack()

etiqueta=Label(ventana,text="Contraseña")
etiqueta.pack()
text_contraseña=Entry(ventana)
text_contraseña.config(bg="Blue",fg="white",show="*")
text_contraseña.pack()


boton_evaluar=Button(ventana,text="Evaluar",command=evaluar_datos)
boton_evaluar.pack()


ventana.mainloop()

