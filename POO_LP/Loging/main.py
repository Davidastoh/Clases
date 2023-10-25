# impoortar mi base de datos
# Crear clase para el usurio
# metodos
# actualizar edad 
# verificar si el usuario si esta registrado o existe en mi registro 
# validar usuario y password


# class Usuario:
#     def _init_(self, nombre, edad, fecha_nacimiento, dni, usuario, password):
#         self.nombre = nombre
#         self.edad = edad
#         self.fecha_nacimiento = fecha_nacimiento
#         self.dni = dni
#         self.usuario = usuario
#         self.password = Password
#         self.registrado = False

#     def actualizar_edad(self, nueva_edad):
#         self.edad = nueva_edad

#     def verificar_registro(self):
#         if self.registrado:
#             print("El usuario está registrado.")
#         else:
#             print("El usuario no está registrado.")

#     def validar_usuario_password(self, usuario, password):
#         if self.usuario == usuario and self.password == password:
#             print("El usuario y contraseña son válidos.")
#         else:
#             print("El usuario y contraseña no son válidos.")
            
# Usuario = usuario("86576452","Max","24/12/2011","Admin","1634")
# Usuario.verificar_registro()
# Usuario.registrado = True
# Usuario.validar_usuario_password("", "")

from datetime import *
from bd import *

def calcular_edad(fecha_nacimiento):
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    if fecha_nacimiento.month > fecha_actual.month or (fecha_nacimiento.month == fecha_actual.month and fecha_nacimiento.day > fecha_actual.day):
        return edad

for usuario in usuario:
    fecha_nacimiento= datetime.striptime(usuario["f_nacimiento"],"%d/%m/%Y")
    usuario["edad"] = int((datetime.now() == fecha_nacimiento).days/365)
print(Usuarios)
dni_buscar=12345678

print(any(u["dni"] == dni_buscar for u in Usuarios))
dni_validar=98765432
password_validar="qwerty123"
print(any(u["dny"] == dni_validar and u["password"] == password_validar for u in Usuarios))
