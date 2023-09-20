
FUNCIONES DE PYTHON MAS USADAS

1. `print()` : Se utiliza para imprimir mensajes o valores en la consola.
2. `len()` : Devuelve la longitud (cantidad de elementos) de un objeto iterable, como una cadena, lista o tupla.
3. `input()` : Se utiliza para obtener la entrada del usuario desde la consola.
4. `range()` : Genera una secuencia de números dentro de un rango especificado.
5. `str()` ,  `int()` ,  `float()` : Estas funciones se utilizan para convertir valores a cadenas, enteros o números de punto flotante, respectivamente.
6. `type()` : Devuelve el tipo de datos de un objeto.
7. `list()` ,  `tuple()` ,  `dict()` ,  `set()` : Estas funciones se utilizan para crear listas, tuplas, diccionarios y conjuntos, respectivamente.
8. `max()` ,  `min()` : Devuelven el valor máximo y mínimo de una secuencia de valores.
9. `sum()` : Devuelve la suma de los elementos de una secuencia de números.
10. `sorted()` : Devuelve una lista ordenada de elementos de una secuencia.
11. `abs()` : Devuelve el valor absoluto de un número.
12. `round()` : Redondea un número al número entero más cercano

ENTORNOS VIRTUALES EN PYTHON


Los entornos virtuales en Python son herramientas que permiten crear entornos aislados para desarrollar y ejecutar proyectos de Python de manera independiente. Estos entornos virtuales contienen su propia instalación de Python y paquetes, lo que permite tener diferentes versiones de Python y paquetes en diferentes proyectos sin conflictos.

Los entornos virtuales son especialmente útiles cuando se trabaja en proyectos con diferentes dependencias o versiones de paquetes. Al utilizar un entorno virtual, puedes instalar y gestionar las dependencias específicas de cada proyecto sin afectar al sistema global de Python.

En Python, hay varias herramientas populares para crear y gestionar entornos virtuales, como:

- `venv` : Es el módulo de Python incorporado para crear entornos virtuales. Se puede utilizar ejecutando el comando  `python -m venv nombre_del_entorno`  en la línea de comandos.
- `virtualenv` : Es una herramienta externa que también permite crear y gestionar entornos virtuales. Se puede instalar utilizando  `pip`  mediante el comando  `pip install virtualenv` .

Una vez que se ha creado un entorno virtual, se puede activar utilizando el comando adecuado según la herramienta utilizada. Por ejemplo, con  `venv` , se puede activar el entorno virtual ejecutando  `source nombre_del_entorno/bin/activate`  en sistemas Unix o  `nombre_del_entorno\Scripts\activate`  en Windows.

Una vez activado el entorno virtual, todas las instalaciones de paquetes y ejecuciones de Python se realizarán en ese entorno aislado. Esto permite mantener un control más preciso sobre las dependencias y versiones utilizadas en cada proyecto.

Es recomendable utilizar entornos virtuales en Python para mantener proyectos limpios y evitar conflictos entre dependencias.
