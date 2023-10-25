# impoortar mi base de datos
from bd import *
# Crear clase para el usurio
# metodos
# actualizar edad 
# verificar si el usuario si esta registrado o existe en mi registro 
# validar usuario y password

class Usuario:
    def _init_(self, nombre, edad, fecha_nacimiento, dni, usuario, password):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.dni = dni
        self.usuario = usuario
        self.password = password
        self.registrado = False

    def actualizar_edad(self, nueva_edad):
        self.edad = nueva_edad

    def verificar_registro(self):
        if self.registrado:
            print("El usuario está registrado.")
        else:
            print("El usuario no está registrado.")

    def validar_usuario_password(self, usuario, password):
        if self.usuario == usuario and self.password == password:
            print("El usuario y contraseña son válidos.")
        else:
            print("El usuario y contraseña no son válidos.")
            
usuario1 = Usuario("Adan", 18, "25/10/2003", 74374328, "Adan", "1234")
usuario1.verificar_registro()
usuario1.registrado = True
usuario1.validar_usuario_password("Adan", "5678")
