from tkinter import *
from tkinter.messagebox import *
import orm
from Tablas.Usuarios import Usuarios
db = orm.SQLiteORM("EstudiantesJMA")
db.crear_tabla(Usuarios)

def f_limpiar(ventana):
    ventana.nombre_texto.delete(0,END)
    ventana.apellidos_texto.delete(0,END)
    ventana.celular_texto.delete(0,END)

    ventana.nombre_texto.focus()

def f_nuevo(ventana):
    nombre=ventana.nombre_texto.get()
    apellido=ventana.apellidos_texto.get()
    celular=ventana.celular_texto.get()
    ventana.tabla_datos.insert("",END,text=nombre,values=(apellido,celular))
    date = {
        "Nombre":nombre,
        "Apellido":apellido,
        "Celular":celular
    }
    db.insertarUno('Usuarios',date)
    showinfo(title='save', message='Nuevo registro agregado')
    #nuevo
    id = db.mostrar('Usuarios', where=f'Celular={celular}')[0][0]
    showinfo(title="Nuevo",message="Nuevo contacto agregado")
    f_limpiar(ventana)

def f_eliminar(ventana):
    item_seleccionado = ventana.tabla_datos.selection()

    if item_seleccionado:
        dato = ventana.tabla_datos.item(item_seleccionado)['text']
        ventana.tabla_datos.delete(item_seleccionado)
        if db.eliminar('Usuarios', where=f'id={dato}'):
            showwarning(title="ELIMINAR", message="Registro eliminado")
        else:
            showerror(title="ERROR", message="Error al eliminar el registro")
        
        f_limpiar(ventana)
    else:
        showinfo(title="ADVERTENCIA", message="Selecciona un contacto para eliminar.")

def f_actualizar(ventana):
    if ventana.nombre_texto.get()=="":
        showerror(title="SIN DATOS",message="No hay ningun dato selecionado")
    else:
        nombre=ventana.nombre_texto.get()
        apellidos=ventana.apellidos_texto.get()
        celular=ventana.celular_texto.get()
        elem_actualizar=ventana.tabla_datos.selection()
        date = ventana.tabla_datos.item(elem_actualizar)['text']
        mensaje=askyesno(title="Actualizar",message="Estas seguro que deseas actualizar")
        if mensaje == True:
            f_limpiar(ventana)
            update = {
                'Nombre':nombre,
                'Apellido':apellidos,
                'Celular':celular
                }
            ventana.tabla_datos.selection_remove(elem_actualizar)
            db.actualizar('Usuarios',update,where=f'id={date}')
            return ventana.tabla_datos.item(elem_actualizar,text=nombre,values=(apellidos,celular))
        else:
            showinfo(title="NO ACTUALIZO",message="No se actualizo ningun registro")
            f_limpiar(ventana)
            ventana.tabla_datos.selection_remove(elem_actualizar)

def f_dobleClick(ventana,event):
    elem_actualizar=ventana.tabla_datos.selection()
    captura_datos=ventana.tabla_datos.item(elem_actualizar)
    mensaje=askyesno(title="ACTUALIZAR",message="Desea actualizar los datos")
    if mensaje == True:
        nombre=captura_datos["text"]
        apellidos=captura_datos["values"][0]
        celular=captura_datos["values"][1]
        ventana.nombre_texto.insert(0,nombre)
        ventana.apellidos_texto.insert(0,apellidos)
        ventana.celular_texto.insert(0,celular)
        ventana.tabla_datos.selection_remove(elem_actualizar)
    else:
        showinfo(title="ACTUALIZAR",message="Ningun registro seleccionado para actualizar")
        ventana.tabla_datos.selection_remove(elem_actualizar)