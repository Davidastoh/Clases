from sqlite3 import *

def crearConexion():
    conn=connect("./base_datos/tecnologico.db")
    conn.commit()
    conn.close()

# def crearTablaAlumno():
#     conn=connect("./base_datos/tecnologico.db")
#     cursor=conn.cursor()
#     sentencia="""
#       CREATE TABLE IF NOT EXISTS Alumnos(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre TEXT(250),
#         edad INTEGER
#     )
# """
#     cursor.execute(sentencia)
#     conn.commit()
#     conn.close()
    
# def crearTablaCurso():
#     conn=connect("./Base_Datos/Tecnologico.db")
#     cursor=conn.cursor()
#     sentencia="""
#       CREATE TABLE IF NOT EXISTS Cursos(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre TEXT(250),
#         id_alumno INTEGER,
#         FOREIGN KEY(id_alumno) REFERENCES Alumnos_id
#     )
# """
#     cursor.execute(sentencia)
#     conn.commit()
#     conn.close()

# def insertAlumno(nombre,edad):
#     conn=connect("./Base_Datos/tecnologico.db")
#     cursor=conn.cursor()
#     sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES('{nombre}',{edad})"
#     cursor.execute(sentencia)
#     conn.commit()
#     conn.close()

# def insertAlumnos(lista):
#     conn=connect("./Base_Datos/Tecnologico.db")
#     cursor=conn.cursor()
#     sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES(?,?)"
#     cursor.executemany(sentencia,lista)
#     conn.commit()
#     conn.close()

def EliminarDatos(tabla,condicion):
    conn=connect("./Base_datos/Tecnologico.db")
    cursor=conn.cursor()
    sentencia=f"DELETE FROM {"Alumnos"} WHERE {"1=1"}"
    conn.commit()
    conn.close()

# def ActualizarDatos(tabla,condicion):
#     conn=connect("./Base_datos/Tecnologico.db")
#     cursor=conn.cursor()
#     sentencia=f"DELETE FROM {"Alumnos"} WHERE {"1=1"}"
#     conn.commit()
#     conn.close()

if __name__=="__main__":
    #crearConexion()
    # crearTablaAlumno()
    # crearTablaCurso()
    # insertAlumno('Jory',30)
    # insertAlumno('China',18)
    # Alum=[
    #     ('Jorycha',29),
    #     ('Chinacha',19),
    #     ('monchi',21),
    #     ('Nadinne',18),
    #     ('Viuda negra',300)
    # ]
    # insertAlumnos(Alum)

    #tarea
    #eliminar y actualizar la lista alumno
    EliminarDatos("Alumnos","1=1")