# Problema de las islas

Este es el documento referente a la cuarta actividad, nos plantea un problema que ya habiamos visto con anterioridad y es de las islas, lo que nos dice es que planteemos que tenemos un mapa representado como una matriz, en ella puede haber islas, el procedimiento nos dice que entonces hay que encontrar los fragmentos de islas que halla en el mapa, esto se haria por medio de recursividad, pero bien vamos al problema.

| · | ■ | ■ | · | · | · |
|---|---|---|---|---|---|
| · | · | · | · | ■ | ■ |
| · | · | · | · | · | · |
| · | · | · | · | ■ | · |
| ■ | · | · | · | ■ | ■ |
| ■ | ■ | · | · | · | ■ |
| ■ | ■ | · | · | ■ | ■ |

Bien, en la parte de arriba podemos ver una pequeña representación de lo que seria el mapa, mostrando en el 4 pequeñas islas representadas por cuadrados, la parte de agua o 'no islas' es representada por puntos. A simple vista podemos deducir que hay cuatro islas en el mapa, asi que lo que plantea el problema es encontrar la solución de manera recursiva y mas facil de encontrar las islas en el mapa.

Parece facil si lo planteamos desde ahora, hay que tener bien en cuenta el metodo recursivo que se utilizara, ya que sabemos que los metodos recursivos pueden llegar a ser bucles infinitos y que pueden llegar a causar problemas de rendimiento para nuestro equipo, asi que bien, vamos con las deducciones para asi poder llegar a la solución.

>**Deducción 1:**
>La primer cosa a tener en cuenta es tener en cuenta el tamaño de la matriz o mapa, esto es super importante ya que las funciones encargadas de buscar las islasse rigen por esto mismo, este tamaño bien puede estar dado por el usuario si lo que qeuremos es generar un mapa del tamaño que se desee, puede ser que tambien sea un tamaño fijo puesto por el desarrollador del la solución, o bien puede ser tambien en el caso de que lo que se busque sea extraer datos de una imagen, hoja de datos, tabla, etc. Entonces ahi el tamaño estaria dado por el archivo en cuestión. Para el uso practico yo lo definire como *H* y *W*, como sus siglas en ingles se deduce que me refiero a height y width, asi podemos modificarlas a elección del desarrollador.

$$ H = Alto·del·mapa (Numero·de·filas) $$
$$ W = Ancho·del·mapa (Numero·de·columnas) $$

>**Deducción 2:**
>El segundo factor es la manera de representar en un formato en que se pueda entender y simbolizar a manera de código entre las casillas o posiciones de la matriz que sean tierra (o parte de una isla) y las cuales sean mar o agua (partes que no pertenezcan a una isla). La manera con la cual yo la voy a simbolizar es por numeros, aunque puede hacerse de muchas maneras, a mi me parece mas facil trabajar simbolizando esto con numeros, utilizare el ***0*** para partes del mapa o posiciones en la matriz que se simbolicen como agua, partes del mapa que no pertenecen y delimitan a una isla, el ***1*** para simbolizar las partes del mapa que simbolicen tierra o partes del mapa que sean parte de una isla, este seria el estado inicial que tomaria el mapa, sin ninguna modificacion o alteración por parte de nosotros, pero la cosa no acaba ahi ya que debemos tomar en cuenta que al momento de revisar el mapa e ir verificando casilla por casilla debemos marcar las casillas por las que ya pasamos y fueron revisadas, ya que si vamos a utilizar metodos recursivos no bastara con un ciclo para hacer la revisión ordenada de la matriz, para esto voy a utilizar el numero ***2*** para simbolizar las casillas de la matriz las cuales son partes de tierra o de una isla, pero aparte que ya estan revisadas o son parte de una isla la cual ya fue revisada y descubierta con anterioridad.

$$ 0 = Partes·del·mapa·vacias·(Agua) $$
$$ 1 = Partes·del·mapa·pertenecientes·a·una·isla·(Tierra) $$
$$ 2 = Partes·de·tierra·ya·revisadas·(Tierra·ya·descubierta) $$

>**Deduccion 3:**
>Ahora, como el metodo es recursivo tenemos que ver como se ejecutaria y las restricciones que tiene, para empezar aunque el metodo sea recursivo hay que tener en cuenta que para recorrer la matriz si se va a necesitar de 2 ciclos anidados, los cuales van a iterar las posiciones de la matriz buscando inicialmente una casilla con el valor **1**, al encontrar este valor entraria al metodo recursivo el cual describire en la siguiente deduccion, asi que seria la unica funcion del ciclo anidado, ya que puede haber 2 posibles casos, el primero en donde encuentre la casilla con un valor de **0**, esto pues significaria que no ha encontrado una isla, mismo caso cuando encuentre una casilla con el valor 2, ya que esto significaria que esta celda forma parte de una isla ya descubierta o contada, al final del caso lo que se busca es contar el numero total de islas, al hacer esto nos aseguramos que no se cometa un error contando mas de una vez las islas.

```
for (let i = 0; i < W; i++) {
    for (let j = 0; j < H; j++) {
        if (mapa[i][j]) {
            MetodoRecursivo(i, j);
        }
    }
}
```

>**Deducción 4:**
>Ahora veamos el metodo recursivo, este al estar ya en la validacion tenemos la certeza de que estamos en una casilla perteneciente a una isla, asi que podemos comenzar a buscar casillas alrededor para buscar mas casillas que pertenezcan a la misma isla, asi que lo primero es marcar la casilla actual como casilla descubierta o revisada, como ya lo vimos arriba es con el numero 2. Lo siguiente el hacer uso de la recursividad, La funcion recibe 2 parametros, que son las posiciones en *x* y *y*, asi que si queremos revisar las posiciones alrededor es hacia arriba, abajo, derecha e izquierda.
Otra cosa importante a revisar es los limites del mapa o matriz, para que no nos genere error al hacer esto. Entonces para hacer lo que acabamos de explicar simplemente hay que verificar si las casillas vecinas tienen un valor de 1, asi como verficar que halla mas casillas alrededor o estemos el la orilla del mapa, se haria de la siguiente manera.

```python
function MetodoRecursivo(i, j){
    Mapa[i, j] = 2;

    //Verifica y lanza hacia casilla superior
    if(j>0){
        if(Mapa(i,j-1) == 1){
            MetodoRecursivo(i,j-1);
        }
    }

    //Verifica y lanza hacia casilla inferior
    if(j<H-1){
        if(Mapa(i,j+1) == 1){
            MetodoRecursivo(i,j+1);
        }
    }

    //Verifica y lanza hacia casilla de la izquierda
    if(i>0){
        if(Mapa(i-1,j) == 1){
            MetodoRecursivo(i-1,j);
        }
    }

    //Verifica y lanza hacia casilla de la derecha
    if(i<W-1){
        if(Mapa(i+1,j) == 1){
            MetodoRecursivo(i+1,j);
        }
    }
}
```

>**Deduccion 5:**
>Acabamos de ver como disparar o enviar la funcion recursiva a casillas vecinas, con esto se cubriria que se descubran las casillas que pertenezcan a cada isla, si lo que quieremos es contar las islas que halla en el mapa, lo que se agregaria es una variable contador que sume uno cada vez que encuentra un valor 1, pero no dentro de la funcion recursiva, si no dentro de los ciclos anidados, y asi se asegura que solo se cuente una vez, ya que si analizamos, la iteracion, solo encuentra una casilla de la isla y la recursividad se encarga de encontrar el resto.
A todo esto podemos añadirle varias cosas, como si queremos que nos imprima las posiciones de cada elemento de la isla, podemos añadirlo dentro de la forma recursiva, asi como si queremos encontrar algun color en alguna imagen o algo asi, podemos encontrarla cambiando la validaion, en este caso tratando a una imagen como matriz y cambiando la validacion de 1 por el color (ya sea en decimal o hexadecimal o codigo preferido) deseado.

Esto se va a ver de mejor manera en el archivo Islas.py que se encuentra en esta misma carpeta.
