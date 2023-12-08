# Actividad 6 Flavio Josefo

En esta actividad temos un problema amas complejo, el de Flavio Josefo, omitiremos la historia ya que esa venia escrita ya en el documento de las instrucciones, asi que podemos centrarnos en el problema y la busqueda de la solucion, para empezar hay que recordar lo que se nos pide.
El problema nos pide que dado un cierto numero de personas las cuales estan en circulo, se halle la posición en la cual se puede salvar quedando como ultimo sobreviviente. Ya que si esta en circulo, el primero mataria al de la derecha, el tercero igual, y asi hasta que solo quede uno vivo, la cuestion es encontrar la posicion que nos asegure quedar como ultimos sobrevivientes.

Este problema si me dio un poco de dificultad ya que me tarde demasiado para encontrar el patron que tenian esta sucesion. Para empezar el profesor nos dio como recomendacion el hacerlo con numeros mas chicos, ya que el problema lo plantea con un numero de 41 personas.

Entonces,siendo asi podemos comenzar con las deducciones.

- un jugador = 1🟢
- dos jugadores = 1🟢 2❌ (1 mata 2)

>**Deduccion 1:**
>Podemos comenzar con el numero 1, al ser solo una persona, pues es ella misma la que queda viva, asi que saltariamos a en numero 2, en el tambien se ve que queda vivo el numero 1, ya que mata al 2. Despues de esto las cosas se hacen un poco mas tediosas asi que a continuacion voy a realizar la sucesion de numeros hasta que encuentre la serie o la sucesion que tenga este problema.

> 3 jugadores:

- 1🟢 2🟢 3🟢
- 1🟢 2❌ 3🟢 (1 mata 2)
- 1❌ 2❌ 3🟢 (3 mata 1)

> 4 jugadores:

- 1🟢 2🟢 3🟢 4🟢
- 1🟢 2❌ 3🟢 4🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ (3 mata 4)
- 1🟢 2❌ 3❌ 4❌ (1 mata 3)

> 5 jugadores:

- 1🟢 2🟢 3🟢 4🟢 5🟢
- 1🟢 2❌ 3🟢 4🟢 5🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ 5🟢 (3 mata 4)
- 1❌ 2❌ 3🟢 4❌ 5🟢 (5 mata 1)
- 1❌ 2❌ 3🟢 4❌ 5❌ (3 mata 5)

> 6 jugadores:

- 1🟢 2🟢 3🟢 4🟢 5🟢 6🟢
- 1🟢 2❌ 3🟢 4🟢 5🟢 6🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6🟢 (3 mata 4)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ (5 mata 6)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ (1 mata 3)
- 1❌ 2❌ 3❌ 4❌ 5🟢 6❌ (5 mata 1)

>7 jugadores:

- 1🟢 2🟢 3🟢 4🟢 5🟢 6🟢 7🟢
- 1🟢 2❌ 3🟢 4🟢 5🟢 6🟢 7🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6🟢 7🟢 (3 mata 4)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 (5 mata 6)
- 1❌ 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 (7 mata 1)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 (3 mata 5)
- 1❌ 2❌ 3❌ 4❌ 5❌ 6❌ 7🟢 (7 mata 3)

>8 jugadores:

- 1🟢 2🟢 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢
- 1🟢 2❌ 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6🟢 7🟢 8🟢 (3 mata 4)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8🟢 (5 mata 6)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ (7 mata 8)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7🟢 8❌ (1 mata 3)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ (5 mata 7)
- 1🟢 2❌ 3❌ 4❌ 5❌ 6❌ 7❌ 8❌ (1 mata 5)

>9 jugadores:

- 1🟢 2🟢 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢
- 1🟢 2❌ 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6🟢 7🟢 8🟢 9🟢 (3 mata 4)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8🟢 9🟢 (5 mata 6)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 (7 mata 8)
- 1❌ 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 (9 mata 1)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 8❌ 9🟢 (3 mata 5)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 8❌ 9❌ (7 mata 9)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7❌ 8❌ 9❌ (3 mata 7)

>10 jugadores:

- 1🟢 2🟢 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢
- 1🟢 2❌ 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 (3 mata 4)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8🟢 9🟢 10🟢 (5 mata 6)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10🟢 (7 mata 8)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ (9 mata 10)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ (1 mata 3)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ (5 mata 7)
- 1❌ 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ (9 mata 1)
- 1❌ 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9❌ 10❌ (5 mata 9)

Hasta este punto no he encontrado algun patron, ya que en algunos casos va de 2 en 2, en otros vuelve a 1, esta es la tabla que va hasta ahora:

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|----|
| 1 | 1 | 3 | 1 | 3 | 5 | 7 | 1 | 3 |  5 |

Seguimos con las serie hasta que encuentre la sucesion, que creo que va mas por el lado de los pares e impares, pero veremos mas adelante.

>11 jugadores:

- 1🟢 2🟢 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢
- 1🟢 2❌ 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 (3 mata 4)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8🟢 9🟢 10🟢 11🟢 (5 mata 6)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10🟢 11🟢 (7 mata 8)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 (9 mata 10)
- 1❌ 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 (11 mata 1)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 (3 mata 5)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 8❌ 9❌ 10❌ 11🟢 (7 mata 9)
- 1❌ 2❌ 3❌ 4❌ 5❌ 6❌ 7🟢 8❌ 9❌ 10❌ 11🟢 (11 mata 3)
- 1❌ 2❌ 3❌ 4❌ 5❌ 6❌ 7🟢 8❌ 9❌ 10❌ 11❌ (7 mata 11)

>11 jugadores:

- 1🟢 2🟢 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢
- 1🟢 2❌ 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 (3 mata 4)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 (5 mata 6)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10🟢 11🟢 12🟢 (7 mata 8)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12🟢 (9 mata 10)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ (11 mata 12)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ (1 mata 3)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ 11🟢 12❌ (5 mata 7)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ (9 mata 11)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ (9 mata 11)
- 1🟢 2❌ 3❌ 4❌ 5❌ 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ (1 mata 5)
- 1❌ 2❌ 3❌ 4❌ 5❌ 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ (9 mata 1)

>12 jugadores:

- 1🟢 2🟢 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢
- 1🟢 2❌ 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 (3 mata 4)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 (5 mata 6)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10🟢 11🟢 12🟢 (7 mata 8)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12🟢 (9 mata 10)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ (11 mata 12)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ (1 mata 3)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ 11🟢 12❌ (5 mata 7)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ (9 mata 11)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ (9 mata 11)
- 1🟢 2❌ 3❌ 4❌ 5❌ 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ (1 mata 5)
- 1❌ 2❌ 3❌ 4❌ 5❌ 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ (9 mata 1)

>13 jugadores:

- 1🟢 2🟢 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢
- 1🟢 2❌ 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 (3 mata 4)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 (5 mata 6)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10🟢 11🟢 12🟢 13🟢 (7 mata 8)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12🟢 13🟢 (9 mata 10)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 (11 mata 12)
- 1❌ 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 (13 mata 1)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 (3 mata 5)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 8❌ 9❌ 10❌ 11🟢 12❌ 13🟢 (7 mata 9)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 8❌ 9❌ 10❌ 11🟢 12❌ 13❌ (11 mata 13)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7❌ 8❌ 9❌ 10❌ 11🟢 12❌ 13❌ (3 mata 7)
- 1❌ 2❌ 3❌ 4❌ 5❌ 6❌ 7❌ 8❌ 9❌ 10❌ 11🟢 12❌ 13❌ (11 mata 3)

>14 jugadores:

- 1🟢 2🟢 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢
- 1🟢 2❌ 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 (3 mata 4)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 (5 mata 6)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 (7 mata 8)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12🟢 13🟢 14🟢 (9 mata 10)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14🟢 (11 mata 12)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14❌ (13 mata 14)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14❌ (1 mata 3)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14❌ (5 mata 7)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ 13🟢 14❌ (9 mata 11)
- 1❌ 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ 13🟢 14❌ (13 mata 1)
- 1❌ 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9❌ 10❌ 11❌ 12❌ 13🟢 14❌ (5 mata 9)
- 1❌ 2❌ 3❌ 4❌ 5❌ 6❌ 7❌ 8❌ 9❌ 10❌ 11❌ 12❌ 13🟢 14❌ (13 mata 5)

>15 jugadores:

- 1🟢 2🟢 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢
- 1🟢 2❌ 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢 (3 mata 4)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢 (5 mata 6)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢 (7 mata 8)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12🟢 13🟢 14🟢 15🟢 (9 mata 10)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14🟢 15🟢 (11 mata 12)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14❌ 15🟢 (13 mata 14)
- 1❌ 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14❌ 15🟢 (15 mata 1)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14❌ 15🟢 (3 mata 5)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 8❌ 9❌ 10❌ 11🟢 12❌ 13🟢 14❌ 15🟢 (7 mata 9)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 8❌ 9❌ 10❌ 11🟢 12❌ 13❌ 14❌ 15🟢 (11 mata 13)
- 1❌ 2❌ 3❌ 4❌ 5❌ 6❌ 7🟢 8❌ 9❌ 10❌ 11🟢 12❌ 13❌ 14❌ 15🟢 (15 mata 3)
- 1❌ 2❌ 3❌ 4❌ 5❌ 6❌ 7🟢 8❌ 9❌ 10❌ 11❌ 12❌ 13❌ 14❌ 15🟢 (7 mata 11)
- 1❌ 2❌ 3❌ 4❌ 5❌ 6❌ 7❌ 8❌ 9❌ 10❌ 11❌ 12❌ 13❌ 14❌ 15🟢 (15 mata 7)

>16 jugadores:

- 1🟢 2🟢 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢 16🟢
- 1🟢 2❌ 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢 16🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢 16🟢 (3 mata 4)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢 16🟢 (5 mata 6)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢 16🟢 (7 mata 8)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12🟢 13🟢 14🟢 15🟢 16🟢 (9 mata 10)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14🟢 15🟢 16🟢 (11 mata 12)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14❌ 15🟢 16🟢 (13 mata 14)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14❌ 15🟢 16❌ (15 mata 16)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14❌ 15🟢 16❌ (1 mata 3)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14❌ 15🟢 16❌ (5 mata 7)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ 13🟢 14❌ 15🟢 16❌ (9 mata 11)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ 13🟢 14❌ 15❌ 16❌ (13 mata 15)
- 1🟢 2❌ 3❌ 4❌ 5🟢 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ 13🟢 14❌ 15❌ 16❌ (13 mata 15)
- 1🟢 2❌ 3❌ 4❌ 5❌ 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ 13🟢 14❌ 15❌ 16❌ (1 mata 5)
- 1🟢 2❌ 3❌ 4❌ 5❌ 6❌ 7❌ 8❌ 9🟢 10❌ 11❌ 12❌ 13❌ 14❌ 15❌ 16❌ (9 mata 13)
- 1🟢 2❌ 3❌ 4❌ 5❌ 6❌ 7❌ 8❌ 9❌ 10❌ 11❌ 12❌ 13❌ 14❌ 15❌ 16❌ (1 mata 9)

>17 jugadores:

- 1🟢 2🟢 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢 16🟢 17🟢
- 1🟢 2❌ 3🟢 4🟢 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢 16🟢 17🟢 (1 mata 2)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6🟢 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢 16🟢 17🟢 (3 mata 4)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8🟢 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢 16🟢 17🟢 (5 mata 6)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10🟢 11🟢 12🟢 13🟢 14🟢 15🟢 16🟢 17🟢 (7 mata 8)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12🟢 13🟢 14🟢 15🟢 16🟢 17🟢 (9 mata 10)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14🟢 15🟢 16🟢 17🟢 (11 mata 12)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14❌ 15🟢 16🟢 17🟢 (13 mata 14)
- 1🟢 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14❌ 15🟢 16❌ 17🟢 (15 mata 16)
- 1❌ 2❌ 3🟢 4❌ 5🟢 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14❌ 15🟢 16❌ 17🟢 (17 mata 1)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 8❌ 9🟢 10❌ 11🟢 12❌ 13🟢 14❌ 15🟢 16❌ 17🟢 (3 mata 5)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 8❌ 9❌ 10❌ 11🟢 12❌ 13🟢 14❌ 15🟢 16❌ 17🟢 (7 mata 9)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 8❌ 9❌ 10❌ 11🟢 12❌ 13❌ 14❌ 15🟢 16❌ 17🟢 (11 mata 13)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7🟢 8❌ 9❌ 10❌ 11🟢 12❌ 13❌ 14❌ 15🟢 16❌ 17❌ (15 mata 17)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7❌ 8❌ 9❌ 10❌ 11🟢 12❌ 13❌ 14❌ 15🟢 16❌ 17❌ (3 mata 7)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7❌ 8❌ 9❌ 10❌ 11🟢 12❌ 13❌ 14❌ 15❌ 16❌ 17❌ (11 mata 15)
- 1❌ 2❌ 3🟢 4❌ 5❌ 6❌ 7❌ 8❌ 9❌ 10❌ 11❌ 12❌ 13❌ 14❌ 15❌ 16❌ 17❌ (3 mata 11)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|
| 1 | 1 | 3 | 1 | 3 | 5 | 7 | 1 | 3 |  5 |  7 |  9 | 11 | 13 | 15 |  1 |  3 |

>**Deduccion 2:**
>Creo que he encontrado la sucesion, al ver la tabla de resultados me puse a revisar y hay cierto patron que es de 2 en 2, esto siempre y cuando no caiga en un exponente de 2, ya que al caer en un exponente de 2 se reinicia la cuenta a 1, despues sigue la serie de 2 en 2 hasta encontrar un numero que sea exponente de 2 ejeplo:
$$ 2, 4, 8, 16, 32, 64, 128, ... $$

>**Deduccion final:**
>Entonces al ser asi, ahora podemos ver la funcion programada, lo que a mi se me ocurre es hacer una funcion que tenga un ciclo, primero se daria un numero, en el caso del ejemplo 41, dado ese numero tendria un ciclo, el ciclo se detendria al llegar al numero 41, entonces tendria una variable llamada posicion la cual iniciaria en 1, cada iteracion se le sumaria 2, despues de esa iteracion tendria dentro una condicion, si el numero de ciclo es algun exponente de 2, entonces se reinicia la variable a 1, y asi consecutivamente mientras el ciclo siga, esto se veria mejor programado asi:

```python
def esExponenteDeDos(ronda):
    exponente = 0
    while (2 ** exponente <= ronda):
        if (2 ** exponente == ronda):
            return True
        exponente += 1
    return False
```

```python
for i in range(personas):
    if (esExponenteDeDos(i+1)):
        posicion = 1
    else:
        posicion += 2
print('La persona que se salva es la', posicion)
```

> En los bloques de codigo anterior podemos ver 2 funciones, la primera se llama *esExponenteDeDos*, en esta funcion simplemete valido si el numero de vuelta es un exponente de 2, es un ciclo que empiexa en 0 hasta el numero de ronda, simplemente devuelve *true* o *false*, en caso de que la ronda sea un exponente de 2, si no devuelve falso.

> Despues tenemos la funcion o ciclo principal, este ciclo va de 0 hasta el numero de personas que se le halla indicado, en cada iteracion va aumentando en 2 la variable posicion, esta variable comienza el ciclo en 1, va aumentando de 2 en 2, pero aparte tiene una condicion dentro del ciclo, en cada iteracion se hace uso de la funcion anterior, lo que hace es prenguntar si es un exponente de 2, si lo es reinicia la variable a 1, basicamente lo misma funcion y deduccion a la que llegamos con los ejemplos del inicio.

## Por ultimo para responder a la prengunta, Josefo se sento en la posicion 19
