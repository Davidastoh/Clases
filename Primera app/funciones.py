from tkinter import *
from tkinter.messagebox import *

def f_limpiar(ventana):
    ventana.nombre_texto.delete(0,END)
    ventana.Apellidos_texto.delete(0,END)
    ventana.Celular_texto.delete(0,END)

    ventana.nombre_texto.focus()
def f_nuevo(ventana):
    nombre=ventana.nombre_texto.get()
    apellidos=ventana.Apellidos_texto.get()
    celular=ventana.Celular_texto.get()

    ventana.tabla_datos.insert("",END,text=nombre,values=(apellidos,celular))

    showinfo(title="Nuevo",message="Agregar nuevo contacto")  

    f_limpiar(ventana)

def f_eliminar(ventana):
    elem_eliminar=ventana.tabla_datos.selection()
    ventana.tabla_datos.delete(elem_eliminar)
    showwarning(title="Eliminar", message="Eliminar el contacto")
    # ventana.destroy()

def f_actualizar(ventana):
    if ventana.nombre_texto.get()=="":
        showerror(title="Sin datos",message="No hay ningun dato seleccionado")
    else:
        nombre=ventana.nombre_texto.get()
        apellidos=ventana.Apellidos_texto.get()
        celular=ventana.Celular_texto.get()
        elem_actualizar=ventana.tabla_datos.selection()

        mensage=askyesno(title="Actualizar",message="Estas seguro, que desea actualizar los datos")

        if mensage == True:
            f_limpiar(ventana)
            ventana.tabla_datos.selection_remove(elem_actualizar)
            return ventana.tabla_datos.item(elem_actualizar,text=nombre,values=(apellidos,celular))

        else:
            showinfo(title="Actualizar",message="Ningun registro selecionado para actualizar")
        
            f_limpiar(ventana)
            ventana.tabla_datos.selection_remove(elem_actualizar)
       
        # print(ventana.tabla_datos.item(elem_actualizar))
    


def f_dobleClick(ventana,event):
    elem_actualizar=ventana.tabla_datos.selection()
    cap_datos=ventana.tabla_datos.item(elem_actualizar)
    mensage=askyesno(title="Actualizar",message="Desea actualizar los datos")
    if mensage == True:
        nom=cap_datos["text"]
        ape=cap_datos["values"][0]
        cel=cap_datos["values"][1]

        ventana.nombre_texto.insert(0,nom)
        ventana.Apellidos_texto.insert(0,ape)
        ventana.Celular_texto.insert(0,cel)

        ventana.tabla_datos.selection_remove(elem_actualizar)

    else:
        showinfo(title="Actualizar",message="Ningun dato selecionado para actualizar")
        ventana.tabla_datos.selection_remove(elem_actualizar)