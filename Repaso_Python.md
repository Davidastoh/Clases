# REPASO PYTHON
## 1. TIPOS DE DATOS

## Numericos 
 Python admite diferentes tipos de números, como enteros (int), números de punto flotante (float) y números complejos (complex). 
 
 Ejemplo:
* entero = 10
* flotante = 3.14
*  complejo = 2 + 3j
## De texto
Todo lo que este entre comillas es un string, y puede estar en comillas simples o dobles.
Las cadenas (strings) se utilizan para almacenar texto en Python.
  Se pueden crear utilizando comillas simples ('') o comillas dobles ("").

Ejemplo. 
1. "a"
2. "hola"
3. "como estas"
4.  _Cadena = "Hola, mundo!"_

 
 ## Booleano
 El tipo de dato booleano se utiliza para representar dos valores: Verdadero (True) y Falso (False). Es útil para realizar operaciones lógicas y de comparación. 
 
 Ejemplos de cómo se utilizan los datos booleanos en Python:

    * Verdadero (True):
     python
    verdadero = True_

    * Falso (False):
     python
    falso = False

Los datos booleanos son especialmente útiles en estructuras de control como condicionales y bucles, donde se evalúan expresiones lógicas para tomar decisiones. 

**Por ejemplo:**

    x = 5

    y = 10 
es_mayor = x > y  # False, ya que 5 no es mayor que 10
En este ejemplo, la variable  es_mayor  se establecerá en False porque la expresión lógica  x > y  es falsa. 
## 2. VARIABLES 

Una variable es un nombre que se utiliza para almacenar un valor en la memoria. Las variables en Python se pueden crear asignándoles un valor utilizando el operador de asignación "=". 
Es donde almacenamos los datos, estos datos pueden mutar o modificarse 
 
Cómo se crean variables para almacenar los datos
* **Darle un nombre significativo o relacionado al dato que se va a almacenar**

  _Edad = 19_

* **Crear una variable y asignarle un valor de cadena de caracteres
nombre**

  _="Max"_

- **Imprimir el valor de una variable**
  
   _print(edad)  # Salida: 25_

## 3. OPERADORES
### I. Operadores aritmeticos 

- SUMA -> +
- RESTA -> -
- DiIVISIION -> / 
- MULTIPLICACION -> *

EJEMPLO:
  
    _suma=45+12_
    _resta=45-12_
    _multi=2*5_
     _divi=12/4_

### II. Operadores de uso especial 
- suma=45+12 -> *operador suma resultado 57*
- suma='45'+12 -> *operador concatenacion resultado 4512*
- saludo='hola'+'mundo'*concatenacion holamundo*
- saludo2='hola'+' '+'mundo' -> *concatenar hola mundo*
- saludo3='hola'*2 -> *holahola*

## 4. DATOS ESTRUCTURADOS 
I.  **Listas**
  
 Se puede alamcenar distintos tipos de datos en una sola lista separados por comas . Una lista es una colección ordenada y mutable de elementos. Puede contener elementos de diferentes tipos de datos. 

Ejemplo:

    _Lista=['nombre','10','False']_

    _lista_amigos=['Adan','Max']_

  II. **Objetos**

Tambien al igual que las listas almacenan distintos tipos de datos pero con un orden.
  Para almacenar datos en un objeto necesitamos especificar que indica y un valor *clave->valor*
```python
  Alumno={
    'nombre':'David',
    'edad':'19',
    'amigos':['Adan','Max'],
    'direccion':(
        'departamento':'Ayacucho',
        'provincia':'Lucanas',
        'distrito':'Puquio',
        'jiron':'Jose maria arquedas',
        'numero':123
    )}
```
## 5. CONTROLES DE FLUJOS
### Descisiones.
solo se ejecura si la condicion es verdadera.Podemos hacer que si la condicion sea falsa se ejecute otro codigo.
### sintaxis 
primero especificar el codigo que se ejecutara si cumplo una ciondicion 
```python 
if condicion
```
el codigho que sdeseamos ejecutar si la condicion es verad.
```python
print("ejecuta esto")
```
aqui estamos del if o del si este codigo siempe se ejecutara no depende del if.
```python
print("esto siempre ejecuta")
```
si queremos quew se ejecute un codigo en caso sea falso 
```python
if <condicion falsa>:
  print("solo imprime si es verdad")
else:
  print("si es falso impreme esto")
```
Ejemplitos:

```python
if 15>18:
  print("solo imprime si es verdad")
else:
  print("si es falso impreme esto")
  ```
```python
if 15*2=30:
  print("solo imprime si es verdad")
else:
  print("si es falso impreme esto")
 ```

```python
if condicion=True
 print("imprime esto si es verdad")
else:
  print("impreme esto si es falso")
```
### Ciclos
Existen dos tipos:
* **Iterar cuando sabes la cantidad de veces a repetir**

Para este caso existe el for.

Sintaxis de la palabra reservada for deberemos crear una variables que almacenen El numero que iremos iterando.

Luego tendremos que indicar el rango a iterar a los elementos a iterar.
```python
vocales=["a","e","i","o","u" ]
for i in vocales:
  print(i)
 ```
```python
for i in range(1,5):
  print(i)
```
* **Iterar cuando no sabemos la cantidad de veces a repetir**
Para eso existe el while
```Python
condicion= True
while True:
  print("hola")
  texto=input("ingresa tu nombre o salir para terminar el programa:" )
  if texto== "salir"
     condicion= false
```

#  6. FUNCIONES :blush:
EXISTEN DOS TIPOS DE FUNCIONES:
#### 1. FUNCIONES PROPIAS DEL LENGUAJE:
Que ya vienen creadas e insertadas en python y estan listas para ser usadas.
tiene el nombre seguido de parentesis (), dentro de las parentesis podremos pasar lo0s dastos que necesita la funcion para ejecutarse.

EJEMPLOS:

* PRINT. Esta es una funcion que nos asirver para mostrar por consola los datos.

* LEN. Esta funcion nos permite saber la longitud de una lista o una string.
INPUT. Esta funcion es una que detiene a esperar quer el usuario introduzca la informacion.
Entre parentesis podremos escribir un mensaje de que accion realica el ususario.
#### 2.  