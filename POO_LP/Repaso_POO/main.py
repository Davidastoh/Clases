from rich import print
from rich.markdown import Markdown
#titulo
edad=16
respuesta="[bold blue]es mayor de edad" if edad>17 else "[italic underline purple]es menor de edad"
texto="""
    #parrafo
    '''bash
    git commit -m "Titulo" -m "cuerpo del commit"
    #comentario
    '''
    * lista
    * lista
    > informacion valiosa
    {}
""".format(respuesta)
mostrar_mark = Markdown(texto)
print(mostrar_mark)