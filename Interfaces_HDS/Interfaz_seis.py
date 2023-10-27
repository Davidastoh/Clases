from tkinter import *
ventana=Tk()
ventana.title("clase radiobutton")
ventana.geometry("400x300")
etiqueta=Label(ventana,text="radio buttons")
etiqueta.config(fg="#EB6828",font=50)
etiqueta.pack()
info=IntVar()

info=IntVar()

def mostrar_radio():
    # respuesta = "Eres masculino" if info.get()==1 else "Eres femenino"
    # etiquetaRespuesta=Label(ventana,text=respuesta)
    # etiquetaRespuesta.pack()

    if info.get()==1:
        etiquetaRespuesta=Label(ventana,text="Eres masculino")
        etiquetaRespuesta.pack()

    else:
        etiquetaRespuesta=Label(ventana,text="Eres feminino")
        etiquetaRespuesta.pack()

    print(info.get())

radioMasculino=Radiobutton(ventana,text="Masculino",value=1,variable=info)
radioMasculino.pack()

radioFemenino=Radiobutton(ventana,text="Femenino",value=0,variable=info)
radioFemenino.pack()
# Instanciar la clase button
button=Button(ventana,text="Enviar",command=mostrar_radio)
button.pack()


# def captura_dato():

#     Text=Radiobutton.get()
#     mensaje=Label(ventana,text=f"hola,{Text}")
#     mensaje.pack()

# def mostrar_dato():
#     print(captura_dato)


ventana.mainloop()
###############################################################################################
# tarea
# ingrese un numero
#  

