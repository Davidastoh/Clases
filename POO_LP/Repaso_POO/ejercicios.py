from rich import print
class persona:
    def __init__(self,nombre:str,edad:int,sexo:str):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    
    def commen(self,plato_favorito:str):
        return f"yo {self.nombre} estoy comiendo {plato_favorito}"
    
    def cagar(self):
        return "pipi popo"
    
class estudiante(persona):
    def __init__(self,nombre:str,edad:int,sexo:str,carrera_profesional:str):
        super().__init__(nombre,edad,sexo)
        self.carrera_profesional=carrera_profesional
    def estudiar(self):
        return "estoy estudiando POO"

class trabajador(persona):
    def __init__(self,nombre:str,edad:int,sexo:str,profesion:str):
        super().__init__(nombre,edad,sexo)
        self.profesion=profesion
    def trabajar(self):
        return "estoy trabajando en el IESTP JMA"

persona_estudiante=persona()
persona_estudiante.datos_persona("Jorge",13,"masculino","estudiante de POO")
print(f'[bold purple]'+persona_estudiante.estudiar())
print('[bold purple]'+persona_estudiante.trabaja())
print('[bold purple]'+persona_estudiante.nombre+" "+persona_estudiante.sexo)    

persona_trabajador=persona()
persona_trabajador.datos_persona("Juan",27,"masculino","Profesor")
print(f'[bold green]'+persona_trabajador.trabaja())
print('[bold green]'+persona_trabajador.trabaja())
print('[bold green]'+persona_trabajador.nombre+" "+persona_trabajador.sexo)

