# TKinter
## ¿Que es TKinter?
Tkinter es una biblioteca de Python que proporciona una interfaz gráfica de usuario (GUI) para crear aplicaciones. Es una abreviatura de "Tk interface" y se basa en la biblioteca Tcl/Tk. Tkinter se utiliza comúnmente para desarrollar aplicaciones de escritorio con interfaces gráficas interactivas. Permite crear ventanas, botones, cuadros de texto y otros elementos visuales en Python.
## Modo de uso
Para utilizar Tkinter en Python, primero debes asegurarte de tenerlo instalado. Por lo general, Tkinter ya viene incluido en la instalación estándar de Python, por lo que no es necesario instalarlo por separado. 

Una vez que tienes Tkinter instalado, puedes comenzar a utilizarlo en tus programas de Python. 
Un ejemplo de cómo usar Tkinter para crear una ventana:

- Importamos la biblioteca Tkinter con el alias  tk .
```python
import tkinter as tk
```
### 1.  Crear una ventana
Se crea una ventana, creamos una instancia de la clase  Tk , que representa la ventana principal de nuestra aplicación. Personalizamos la ventana estableciendo un título y una geometría. 
```python
ventana = tk.Tk()
```
### 2. Personalizar la ventana
Personalizamos la ventana estableciendo un título y una geometría.
```python
ventana.title("Mi ventana")
ventana.geometry("400x300")
```

### 3. Agregar elementos a la ventana
Agregamos elementos a la ventana, como una etiqueta de texto y un botón. Utilizamos el método  pack()  para colocar estos elementos en la ventana. 
```python
etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!")
etiqueta.pack()

boton = tk.Button(ventana, text="Haz clic")
boton.pack()
```
### 4. Ejecutar el bucle principal de la ventana
ejecutamos el bucle principal de la ventana con el método  mainloop() , lo que permite que la ventana sea visible y responda a eventos.
```python
ventana.mainloop() 
```

