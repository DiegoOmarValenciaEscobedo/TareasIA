# La Heuristica

La heuristica a lo que he estado invistigando tiene que ver con el hallar o inventar, tambien un poco con la disciplica de encontrar estrategias, reglas, silogismos y conclusiones. Hablando en el caso concreto de este problema podemos decir que la heuristica puede ayudarnos a resolver el problema de los laberintos, en el cual podemos utilizar metodos como la fuerza bruta, o buscar metodos mas efectivos y eficientes para resolverlo, recuerdo que el profesor nos hablo de el algoritmo **A***, el cual es un algoritmo mas eficiente para encontrar el camino o la salida rapidamente.

<div style="text-align:center;">
    <img src="https://i.pinimg.com/originals/2e/f5/ae/2ef5ae2b8c253b6bf8ddae681add7322.png">
</div>

## Metodo Recursivo

Para el primer paso vamos a resolverlo de cierta forma con fuerza bruta, ya que al utilizar el metodo recursivo no se tiene un metodo claro por el cual llegar a la salida, todo tiene que ver con hacer un recorrido completo o parcial hasta encontrar la salida.

Para esto utilizariamos un programa similar al que utilizamos en el problema de las islas, donde buscabamos todas las celdas que conformaban la isla, claro, con algunas modificaciones.

Entonces, ya teniendo en cuenta esto, vamos a ver como queda el metodo:

```phyton
def busqueda(x,y):
    if(encontrado):
        return
    if(laberinto[x][y]==3):
        print('salida encontrada en:',x,y)
        encontrado = True
        return
    if(x<0 or x>8 or y<0 or y>8 or laberinto[x][y]!=0):
        return
    else:
        laberinto[x][y]=2
        print('casilla:',x,y)
        busqueda(x-1,y)
        busqueda(x+1,y)
        busqueda(x,y-1)
        busqueda(x,y+1)

busqueda(1,0)
```

El siguiente codigo es el que yo implemente para realizar una busqueda sencilla por el metodo de recursividad, para ello primero hay que tener definidas 2 variables, la primera es una matriz con el laberinto, o en caso de que se trabaje con imagenes, pues definir la imagen junto con sus medidas, en mi caso yo defini la matriz de 9*9 que es la misma que se muestra en la imagen de arriba.
La segunda variable es una booleana, la funcion de esta es como punto de referencia para saber cuando se encuentre la salida entonces las demas ramas que se desprenden en la recursividad ya no sigan buscando y se ahorre tiempo de ejecucion.
Ya sabiendo esto, la funcion **busqueda** recibe 2 parametros, que son las coordenadas de la celda o el punto en el laberinto, dentro de la funcion en su mayoria son validaciones if, la primera valida si no se ha encontrado ya la salida, en alguna de las ramificaciones que se generan con las llamadas recursivas, la segunda validacion verifica si la celda actual es la salida, para mi caso la salida del mapa la marque con un *3*, pero puede ser marcada con el valor que se guste o desee, en caso de que la encuentre cambia la variable encontrado a **True** y para la busqueda, la tercera validacion se encarga de verificar que no se encuentre fuera del mapa, en cuano a dimensiones para que no nos de error.
En caso de que no entre en nunguna de las validaciones entonces pasa a la funcion por default, en este caso marca la casilla con el valor *2*, esto significa que ya paso por esa casilla y no volvera a pasar, despues manda a los 4 puntos cardinales la funcion, para seguir la busqueda.
Se me olvido comentar que dentro de la tercera validacion que es donde tambien valida si el valor de la casilla es *0*, esto ya que yo utilice una matriz que inicialmente contiene solo numeros 1 y 0, aparte de la casilla con el numero 3 que es la salida.
Siendo *0* el camino libre o sendero, *1* pared o limite, *2* camino ya explorado y *3* salida. La matriz se veria algo asi:



>|L|A|B|E|R|I|N|T|O|
>|-|-|-|-|-|-|-|-|-|
>|1|1|1|1|1|1|1|1|1|
>|0|0|0|0|0|0|1|0|1|
>|1|1|1|0|1|1|1|0|1|
>|1|0|0|0|1|0|1|0|1|
>|1|0|1|1|1|0|1|0|1|
>|1|0|0|0|0|0|0|0|1|
>|1|0|1|1|1|0|1|0|1|
>|3|0|1|0|0|0|1|0|1|
>|1|1|1|1|1|1|1|1|1|

## Algoritmo de solucion

Bien, se nos pide tambien encontrar un algoritmo de solucion que deseemos, la verdad a mi me parecio optimo el metodo recursivo que implemente anteriormente, pero viendo que debemos escoger otro, pues me iria por el metodo de la mano derecha, que es uno de los que recuerdo que el profesor nos comento, consiste en tocar siempre la pared con la mano derecha y caminar hacia adelante, en algun punto llegaremos a la salida ya que estariamos recorriendo todo el mapa en cierto sentido.

Aquí está el código que implementa el Método de la Mano Derecha:

```python
sentido = 'r'
laberinto = [
    [1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,1,0,1],
    [1,1,1,0,1,1,1,0,1],
    [1,0,0,0,1,0,1,0,1],
    [1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,0,1],
    [3,0,1,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1]
]
# empieza en laberinto[1][0]

def verifica(x, y):
    if(x < 0 or x > 8 or y < 0 or y > 8 or laberinto[x][y] == 1):
        return False
    else:
        return True

def derecha(x, y):
    global sentido
    if(sentido == 'r'):
        if(verifica(x + 1, y)):
            sentido = 'd'
            return x + 1, y
        elif(verifica(x, y + 1)):
            return x, y + 1
        elif(verifica(x - 1, y)):
            sentido = 'u'
            return x - 1, y
        elif(verifica(x, y - 1)):
            sentido = 'l'
            return x, y - 1
    elif(sentido == 'd'):
        if(verifica(x, y - 1)):
            sentido = 'l'
            return x, y - 1
        elif(verifica(x + 1, y)):
            return x + 1, y
        elif(verifica(x, y + 1)):
            sentido = 'r'
            return x, y + 1
        elif(verifica(x - 1, y)):
            sentido = 'u'
            return x - 1, y
    elif(sentido == 'l'):
        if(verifica(x - 1, y)):
            sentido = 'u'
            return x - 1, y
        elif(verifica(x, y - 1)):
            return x, y - 1
        elif(verifica(x + 1, y)):
            sentido = 'd'
            return x + 1, y
        elif(verifica(x, y + 1)):
            sentido = 'r'
            return x, y + 1
    elif(sentido == 'u'):
        if(verifica(x, y + 1)):
            sentido = 'r'
            return x, y + 1
        elif(verifica(x - 1, y)):
            return x - 1, y
        elif(verifica(x, y - 1)):
            sentido = 'l'
            return x, y - 1
        elif(verifica(x + 1, y)):
            sentido = 'd'
            return x + 1, y

def mano_derecha(x, y):
    global sentido
    if(laberinto[x][y] == 3):
        print('salida encontrada en:', x, y)
        return
    else:
        print('casilla:', x, y)
        xs, ys = derecha(x, y)
        mano_derecha(xs, ys)

mano_derecha(1, 0)
```
Este código comienza en la posición (1, 0) del laberinto, con la dirección inicial hacia la derecha (sentido = 'r'). Luego, utiliza la función derecha(x, y) para determinar la próxima casilla en la dirección actual y luego actualiza las coordenadas. La función verifica(x, y) se utiliza para verificar si la próxima casilla es válida. Cuando encuentra la salida, imprime el mensaje y finaliza. La función mano_derecha(x, y) llama a derecha(x, y) y se llama a sí misma recursivamente hasta que encuentra la salida o queda atrapada en un bucle.
Se que es un poco larga y redundante la funcion **derecha**, pero es parte fundamental para que el algoritmo funcione.
