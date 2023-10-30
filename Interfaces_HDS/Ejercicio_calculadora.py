from tkinter import *
ventana = Tk()
ventana.geometry("300x300")
ventana.title("Calculadora")

# clase operadores

class Operadores:
    def sumar(self,num1,num2):
        return num1+num2
    def restar(self,num1,num2):
        return num1+num2
    def multiplicar(self,num1,num2):
        return num1+num2
    def dividir(self,num1,num2):
        return num1+num2
    
# Manejador de operadores

operacion=StringVar()
classOperadores=Operadores()
def manejadorOperaciones():
    num1=int(textoUno.get())
    num2=int(textoDos.get())
    ope=operacion.get()
    if ope=="Suma":
        resultado=classOperadores.sumar(num1,num2)
        Label(ventana,text=f"El resultado de la suma es: 
        {resultado}").pack()
    elif ope=="Resta":
        resultado=classOperadores.restar(num1,num2)
        Label(ventana,text=f"El resultado de la resta es: 
        {resultado}").pack()
    elif ope=="Multiplicacion":
        resultado=classOperadores.multiplicar(num1,num2)
        Label(ventana,text=f"El resultado de la multiplicacion es: 
        {resultado}").pack()
        resultado=classOperadores.dividir(num1,num2)
        Label(ventana,text=f"El resultado de la division es: 
        {resultado}").pack()


etiquetaNumno=Label(ventana,text="Ingresa un numero",value="Suma"variable=operacion)



etiquetaResultado=Label(ventana,text"El resultado es: ")
operacion=StringVar()

operacionSuma=radioButton(ventana,text="Suma",value="Suma"variable=operacion).pack()

boton_Calcular=Button(ventana,text="Calcular")
command
