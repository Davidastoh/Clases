from tkinter import*
def enviar_boton(ventana,valor):
    if valor == "=":
        try:
            expression=ventana,caja_operaciones.get().replace("%","/100")
            resultado=eval(expression)
            ventana.caja_operaciones.delete(0,END)
            ventana.caja_operaciones.insert(0,str(resultado))
            operacion=expression+" "+valor
            ventana.operacion_label.config(text=operacion)
            
            ventana.operacion_label.config(text=operacion)
        except Exception as a:
            ventana.caja_operaciones.delete(0,END)
            ventana.caja_operaciones.insert(0,"error")
            ventana.operacion_label.config(text="")
    elif valor == "C":
        ventana.caja_operaciones.delete(0,END)
        ventana.operacion_label.config(text="")
        
    elif valor == "<":
        valor_actual=ventana.caja_operaciones.get()
        if valor_actual:
            nuevo_valor=valor_actual[:-1]
            ventana.caja_operaciones.delete(0,END)
            ventana.caja_operaciones.insert(0,nuevo_valor)
            ventana.operacion_label.config(text=nuevo_valor+" ")
    else:
        valor_actual=ventana.caja_operaciones.get()
        ventana.caja_operaciones.delete(0,END)
        ventana.caja_operaciones.insert(0,valor_actual+valor)
        if valor == "=":
            ventana.operacion_label.config(text="")
    


