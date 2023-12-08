## Buscar e imprimir color en imagen

Bien, ahora el probelma que nos plantean es un poco mas complejo a lo que manejamos con anterioridad, como sabemos con anterioridad realizamos el programa para encontrar islas en una matriz dada, usando un metodo recursivo para descubrir de un solo jalon todas las celdas que pertenecian a la isla ya descubierta, ahora podemos utilizar las bases de la resolucion de ese problema para usarlo en este. La imagen que utilizaremos para el problema es dada por el profesor y se ve en la parte de abajo, asi que a continuacion podemos hacer algunas deducciones de esto.

<div style="text-align:center;">
    <img src="ImagenActividad5.jpg">
</div>

>**Deducción 1:**
> La primera deduccion que podemos hacer es definir el color a buscar en la imagen, el problema nos dice que el rojo, pero si analizamos la imagen podemos ver que hay varios tonos de rojo, asi que vamos a ver en codigo RGB de los colores rojos.

> El color rojo puro en hexadecimal es:

$$RGB(255,0,0)$$

<div style="background-color: rgb(255,0,0); padding: 10px; text-align: center;">
    <p>Rojo puro.</p>
</div>

> Aunque el color rojo puro es el anteriormente visto hay un rango de colores en rojo que llegan al cafe, pero aun siendo rojos estos empiezan a partir del:

$$RGB(100,0,0)$$

<div style="background-color: rgb(100,0,0); padding: 10px; text-align: center;">
    <p>Rojo mas obscuro.</p>
</div>

> Vemos que aunque el color anteriormente mostrado se asemeja mas a un cafe pues en cierto punto es rojo, asi que ese seria el limite inferior dentro del rango de rojos, y nos queda delimitar el limite superior, lo que serian los rojos mas claros, llegando al naranja, este limite se alcanza con el color:
$$RGB(255, 100, 100)$$

<div style="background-color: rgb(255, 50, 50); padding: 10px; text-align: center;">
    <p>Rojo mas claro.</p>
</div>

>Ya definidos los limites podemos continuar con el siguiente paso.

>**Deducción 2:**
> La segunda cuestión es ver que modificaciones le vamos a hacer al programa que construimos en la actividad anterior, si lo revisamos vamos a trabajar con el metodo iterativo y recursivo. Lo mas sencillo es por el metodo recursivo, ya que lo que se nos pide es contar los elementos de color rojo, asi que podriamos tomar el mismo metodo recursivo utilizado en el programa anterior y hacer algunas modificaciones, para empezar creo que seria buena opcion imprimir los elementos que se encuentran, como hacer un filtro, en dado caso que se encuentre un elemento en el rango de los rojos pues se imprime y despues dispara el metodo recursivo, que al final de cuentas haria lo mismo. Aqui dejo explicado no en codigo final como tal pero lo que se haria conceptualmete.

```
for i in range(w):
    for j in range(h):
        if(esRojo(i, j)):
            islas += 1
            metodoRecursivo(i, j);
```

```
def esRojo(i, j):
    if(filtro[i, j][2] >= r1 and filtro[i, j][2] <= r2):
        if(filtro[i, j][1] >= g1 and filtro[i, j][1] <= g2):
            if(filtro[i, j][0] >= b1 and filtro[i, j][0] <= b2):
                return True;
    return False;
```

```
def metodoRecursivo(i, j):
    if not(i < 0 or i >= w or j < 0 or j >= h):
        if(esRojo(i,j)):
            filtro[i,j][2] = 0
            filtro[i,j][1] = 0
            filtro[i,j][0] = 0
            metodoRecursivo(i - 1, j)
            metodoRecursivo(i + 1, j)
            metodoRecursivo(i, j - 1)
            metodoRecursivo(i, j + 1)
    return
```
>Podemos ver que es muy similar a la funcion que definimos en la actividad anterior, se añadirian algunas funciones como la de **esRojo** que la usaria para validar si el valor de la casilla se encuentra entre el rango de rojos que definimos con anterioridad.

>**Deducción 3:**
> La tercera deduccion viene ya que al estar planteando las anteriores creo que es mas viable hacer una copia de la imagen para trabajar con ella, para asi poder modificar los datos, ya que al haber pasado por las casillas hay que cambiar el valor, esto para que no contemos o tomemos el valor varias veces y pueda contarnos mas de una vez la funcion.

> Esto se vera de mejor manera en el Archivo 'Actividad 5 Rojos.py' donde se encontrara el programa que se encargara de realizar todo esto, cree una imagen llamada filtro en la cual cada pixel que encuentro dentro del rango de rojos lo convierto a negro para poder ver si es que agarro todo el rango de valores que quiero.
