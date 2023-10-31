# impoortar mi base de datos
# Crear clase para el usurio
# metodos
# actualizar edad 
# verificar si el usuario si esta registrado o existe en mi registro 
# validar usuario y password

from datetime import*
from bd import *
class Usuario:
    def __init__(self, DNI, Nombre, F_nacimiento, Edad,Usuario, Password):
        self.DNI=DNI
        self.Nombre=Nombre
        self.F_nacimiento=F_nacimiento
        self.Edad=Edad
        self.Usuario=Usuario
        self.Password=Password

    def mostrar_usuario(self, ide):
        resultado=list(filter(lambda par:par['DNI']==ide,usuarios))
        return f'''Aqui tienes los datos del usuario que buscaste:
        {resultado}'''
    
    def agregar_edad(self, clave, valor):
        for usuario in usuarios:
            if usuario['DNI'] == self.DNI:
                usuario[clave] = valor
                return 'Se actualizó.'
        return 'Usuario no encontrado.'

    def verificar_usuario(self, usuario_buscar):
        for usuario in usuarios:
            if usuario['Usuario'] == usuario_buscar:
                return 'Usuario registrado.'
        return 'Usuario no encontrado en los registros.'

    def validar_usuario_password(self, usuario_a_validar, password_a_validar):
        for usuario in usuarios:
            if usuario['Usuario'] == usuario_a_validar and usuario['Password'] == password_a_validar:
                return 'Usuario y contraseña válidos.'
        return 'Usuario o contraseña incorrectos.'    

    def actualizar_usuario(self, nombre=None, f_nacimiento=None, edad=None, usuario=None, password=None):
        if nombre:
            self.Nombre = nombre
        if f_nacimiento:
            self.F_nacimiento = f_nacimiento
        if edad:
            self.Edad = edad
        if usuario:
            self.Usuario = usuario
        if password:
            self.Password = password

        return 'Usuario actualizado exitosamente.'

actu = Usuario(74484162, "Adan", "10/12/2003", None, "AHC", "0717")
print(actu.actualizar_usuario(nombre="Adam", edad=18, usuario="AHC123", password="newpassword"))

actu=Usuario(74484162,"Adan","10/12/2003",None,"AHC","0717")
print(actu.agregar_edad("edad", 20))
print(actu.mostrar_usuario(74484162))

usuario_a_buscar = "AHC"
print(actu.verificar_usuario(usuario_a_buscar))
print(actu.mostrar_usuario(74484162))

usuario_a_validar = "AHC"
password_a_validar = "0717"
print(actu.validar_usuario_password(usuario_a_validar, password_a_validar))
print(actu.mostrar_usuario(74484162))




