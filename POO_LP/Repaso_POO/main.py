# from rich import print
# from rich.markdown import Markdown
# #titulo
# edad=16
# respuesta="[bold blue]es mayor de edad" if edad>17 else "[italic underline purple]es menor de edad"
# texto="""
#     #parrafo
#     '''bash
#     git commit -m "Titulo" -m "cuerpo del commit"
#     #comentario
#     '''
#     * lista
#     * lista
#     > informacion valiosa
#     {}
# """.format(respuesta)
# mostrar_mark = Markdown(texto)
# print(mostrar_mark)
#########################################################################################################

# print(boby.nombre)

# class Perro:
#     Especie="animal"
#     def __init__(self,edad):
#         self.nombre="edwin"
#         self.edad=edad

#     def ingresar_datos(self,nombre,edad):
#         self.nombre=None
#         self.edad=None

#     def hablar(self):
#         return "Guauuu Guauuu"

# boby=Perro("boby",15):
# print(boby.hablar())
# print(boby.Especie)
# boby.ingresar_datos("edwin",14)
# print(boby.nombre)

# luna=Perra()
# print(luna.hablar())
# luna.ingresar_datos("luna",5)
# print(luna.nombre)
# print(luna.edad)
#########################################################################################################
from rich import print
class mascota:
    def __init__(self):
        self.nombre=None
        self.edad=None
        self.tipo_animal=None
    def hablar(self,sonido):
        return sonido

    def datos_mascota(self,nombre,edad,tipo_animal):
        self.nombre=nombre
        self.edad=edad
        self.tipo_animal=tipo_animal

class Perro(mascota):
    def atacar(self):
        return "ladra y muerde"
class Gata(mascota):
    def atacar(self):
        return "Rasguña a arañazos"

perro_boby=Perro()
perro_boby.datos_mascota("boby",14,"perro")
print(f'[bold green]'+perro_boby.hablar("Guauuu Guauuu"))
print('[bold green]'+perro_boby.atacar())
print('[bold green]'+perro_boby.nombre+" "+perro_boby.tipo_animal)

gata_persa=Gata()
gata_persa.datos_mascota("Persa",13,"gato")
print(f'[bold purple]'+gata_persa.hablar("Miauu Miauu"))
print('[bold purple]'+gata_persa.atacar())
print('[bold purple]'+gata_persa.nombre+" "+gata_persa.tipo_animal)