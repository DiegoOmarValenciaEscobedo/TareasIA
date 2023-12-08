# Problema de los alfiles

En este problema se busca analizar y buscar el numero minumo de movimientos en el cual se pueda pasar todos los alfiles de un lado al otro invirtiendo las posiciones, es decir, si tenemos los alfiles blancos debajo y los negros en la parte de arriba, entonces lo que se busca es que los alfiles negros queden en la parte inferior y que los alfiles blancos queden en la parte superior, esto junto con buscar el camino mas corto o el numero minimo de movimientos.

Bien, para esto hay que tener varias consideraciones y reglas para poder hacer el analisis y la posible solución:

>1. Los alfiles solo se pueden mover en diagonal, no hacia enfrente ni atras, tampoco a los lados, solo diagonal.
>2. El tablero es un rectangulo de 4 casillas de ancho por 5 casillas de alto.
>3. Los turnos son alternados, no importa quien empiece ya que es uno y uno en los turnos.

Esta es la representación del tablero con el cual se trabajaría.
> | ♝ | ♝ | ♝ | ♝ |
>|---|---|---|---|
>| * | * | * | * |
>| * | * | * | * |
>| * | * | * | * |
>| ♝ | ♝ | ♝ | ♝ |

Teniendo esto en cuenta ahora podemos comenzar a plantear una posible solución.
Si tenemos en cuenta que es un tablero de 5 casillas de alto pues podemos deducir que el numero minimo de movimientos por alfil es de 4, ya que al moverse en diagonal ocuparian solo cuatro movimientos para quedar en el final.

Entonces a continuacion voy a poner algunas cosas que deduje del problema y que nos ayudaran a realizar la dedicción final del problema.

> **Deducción 1:**
> Lo primero es que a cada pieza le tomaria 4 movimientos en diagonal, llendo solo hacia adelante, para tomar el lugar del alfil contrario. Esto ya que se busca el minimo numero de movimientos para realizar esta tarea, en la siguiente tabla se muestra enumeradas las casillas con los movimientos casilla por casilla del alfil, esto tambien depende de la posición inicial del alfil, pero eso lo vemos en la deducción 2, al mismo tiempo estos mismos movimeintos funcionan a la inversa, con los alfiles contrarios pasa lo mismo, solo es cosa de voltear el tablero.

Esta es la tabla de movimientos enumerados partiendo desde la posición [0,0].

>> |♝ | * | * | * |
>> |---|---|---|---|
>> | * | 1 | * | * |
>> | 2 | * | 2 | * |
>> | * | 3 | * | 3 |
>> | 4 | * | 4 | * |

Esta es la tabla de movimientos enumerados partiendo desde la posición [0,1].

>> | * |♝ | * | * |
>> |---|---|---|---|
>> | 1 | * | 1 | * |
>> | * | 2 | * | 2 |
>> | 3 | * | 3 | * |
>> | * | 4 | * | 4 |

Esta es la tabla de movimientos enumerados partiendo desde la posición [0,2].

>> | * | * |♝ | * |
>> |---|---|---|---|
>> | * | 1 | * | 1 |
>> | 2 | * | 2 | * |
>> | * | 3 | * | 3 |
>> | 4 | * | 4 | * |

Esta es la tabla de movimientos enumerados partiendo desde la posición [0,3].

>> | * | * | * | ♝|
>> |---|---|---|---|
>> | * | * | 1 | * |
>> | * | 2 | * | 2 |
>> | 3 | * | 3 | * |
>> | * | 4 | * | 4 |

> **Deduccion 2:**
> La deducción 2 parte de la uno, como bien dijimos la posición de partida es importante para predecir en que posición posible puede terminar, ya que un alfil que esta en las posiciones [0, 0] ó [0, 2] solo puede terminar en 2 posibles casillas, ya sea en la [4, 0] ó en la [4, 2]. Lo mismo pasa con las filas 1 y3, los alfiles que ahi comienzan tambien terminaran en unas de esas 2 filas.

> **Deduccion 3:**
> La tercera deducción es que para evitar bloqueos y mantenerlo lo mas optimo seria viable que dependiendo de que pieza se mueve primero en un lado deberiamos mover la pieza contraria de cualquiera de las dos columnas par, o sea, si se mueven las piezas [0, 0] ó [0, 2] seria lo mas viable comenzar a mover los alfiles de las casillas [4, 0] ó [4, 2]. Esto haciendolo con la finalidad que los alfiles tomen el lugar de la pieza que se esta moviendo inicialmente y no dejar piezas en medio del tablero para evitar que se hagan bloqueos entre las piezas y no se tengan que retroceder entre piezas porque eso generaria mas movimientos y lo que se busca el numero minimo de movimientos.

> **Deduccion 4:**
> La siguiente deduccion es el numero total de movimientos, como vimos en el primer punto el numero minimo para mover una pieza de un lado al otro es de cuatro movimientos, entonces el numero de movimientos por jugador o lado es de 16.
>> $$ N_movimientos = 4 * 4 = 16 $$
> Asi que por simple logica solo es multiplicar esto por 2 y nos da 32 movimientos en total, de manera mas optima.
>> $$ N_total = 2 * 16 = 32 $$

> **Deduccion 5:**
> La ultima deducción que seria clave para mantener el margen de el minimo numero de movimientos lo mejor o mas optimo es mover una pieza a la vez, no mover una pieza y luego dejarla enmedio de del tablero ya que puede provocar que halla bloqueos entre las piezas y no se coman estre si.

## Solución
Bien, ya sabiendo todo esto podemos hacer una de las posibles soluciones, ya que como vimos el problema tiene varios caminos para resolverse, dependiendo de quien comienze el juego, asi como si solo se mueve un alfil a la vez o mas de uno, asi como es un poco irrelevante (y a la vez no), sobre la solución, ya que el resultado final al que se busca llegar es el mismo. Todo esto porqeu todos los alfiles de un lado son iguales y es un poco irrelevante el orden de los mismos ya que al final lo que se busca es que queden del lado contrario simplemente.

Asi que bien, esta es la solucion propuesta:

>| ♝₁ | ♝₁ | ♝₁ | ♝₁ |
>|---|---|---|---|
>| * | * | * | * |
>| * | * | * | * |
>| * | * | * | * |
>| ♝₂ | ♝₂ | ♝₂ | ♝₂ |

>| * | ♝₁ | ♝₁ | ♝₁ |
>|---|---|---|---|
>| * | ♝₁ | * | * |
>| * | * | * | * |
>| * | * | * | * |
>| ♝₂ | ♝₂ | ♝₂ | ♝₂ |

>| * | ♝₁ | ♝₁ | ♝₁ |
>|---|---|---|---|
>| * | ♝₁ | * | * |
>| * | * | * | * |
>| * | ♝₂ | * | * |
>| ♝₂ | ♝₂ | * | ♝₂ |

>| * | ♝₁ | ♝₁ | ♝₁ |
>|---|---|---|---|
>| * | * | * | * |
>| * | * | ♝₁ | * |
>| * | ♝₂ | * | * |
>| ♝₂ | ♝₂ | * | ♝₂ |

>| * | ♝₁ | ♝₁ | ♝₁ |
>|---|---|---|---|
>| * | * | * | * |
>| ♝₂ | * | ♝₁ | * |
>| * | * | * | * |
>| ♝₂ | ♝₂ | * | ♝₂ |

>| * | ♝₁ | ♝₁ | ♝₁ |
>|---|---|---|---|
>| * | * | * | * |
>| ♝₂ | * | * | * |
>| * | * | * | ♝₁ |
>| ♝₂ | ♝₂ | * | ♝₂ |

>| * | ♝₁ | ♝₁ | ♝₁ |
>|---|---|---|---|
>| * | ♝₂ | * | * |
>| * | * | * | * |
>| * | * | * | ♝₁ |
>| ♝₂ | ♝₂ | * | ♝₂ |

>| * | ♝₁ | ♝₁ | ♝₁ |
>|---|---|---|---|
>| * | ♝₂ | * | * |
>| * | * | * | * |
>| * | * | * | * |
>| ♝₂ | ♝₂ | ♝₁ | ♝₂ |

>| ♝₂ | ♝₁ | ♝₁ | ♝₁ |
>|---|---|---|---|
>| * | * | * | * |
>| * | * | * | * |
>| * | * | * | * |
>| ♝₂ | ♝₂ | ♝₁ | ♝₂ |
>> **Aqui tenemos las primeras 2 piezas intercambiadas**

>| ♝₂ | ♝₁ | ♝₁ | * |
>|---|---|---|---|
>| * | * | ♝₁ | * |
>| * | * | * | * |
>| * | * | * | * |
>| ♝₂ | ♝₂ | ♝₁ | ♝₂ |

>| ♝₂ | ♝₁ | ♝₁ | * |
>|---|---|---|---|
>| * | * | ♝₁ | * |
>| * | * | * | * |
>| ♝₂ | * | * | * |
>| ♝₂ | * | ♝₁ | ♝₂ |

>| ♝₂ | ♝₁ | ♝₁ | * |
>|---|---|---|---|
>| * | * | * | * |
>| * | * | * | ♝₁ |
>| ♝₂ | * | * | * |
>| ♝₂ | * | ♝₁ | ♝₂ |

>| ♝₂ | ♝₁ | ♝₁ | * |
>|---|---|---|---|
>| * | * | * | * |
>| * | ♝₂ | * | ♝₁ |
>| * | * | * | * |
>| ♝₂ | * | ♝₁ | ♝₂ |

>| ♝₂ | ♝₁ | ♝₁ | * |
>|---|---|---|---|
>| * | * | * | * |
>| * | ♝₂ | * | * |
>| * | * | ♝₁ | * |
>| ♝₂ | * | ♝₁ | ♝₂ |

>| ♝₂ | ♝₁ | ♝₁ | * |
>|---|---|---|---|
>| * | * | ♝₂ | * |
>| * | * | * | * |
>| * | * | ♝₁ | * |
>| ♝₂ | * | ♝₁ | ♝₂ |

>| ♝₂ | ♝₁ | ♝₁ | * |
>|---|---|---|---|
>| * | * | ♝₂ | * |
>| * | * | * | * |
>| * | * | * | * |
>| ♝₂ | ♝₁ | ♝₁ | ♝₂ |

>| ♝₂ | ♝₁ | ♝₁ | ♝₂ |
>|---|---|---|---|
>| * | * | * | * |
>| * | * | * | * |
>| * | * | * | * |
>| ♝₂ | ♝₁ | ♝₁ | ♝₂ |
>> **Aqui tenemos el segundo alfil intercambiada**

>| ♝₂ | * | ♝₁ | ♝₂ |
>|---|---|---|---|
>| * | * | ♝₁ | * |
>| * | * | * | * |
>| * | * | * | * |
>| ♝₂ | ♝₁ | ♝₁ | ♝₂ |

>| ♝₂ | * | ♝₁ | ♝₂ |
>|---|---|---|---|
>| * | * | ♝₁ | * |
>| * | * | * | * |
>| * | * | ♝₂ | * |
>| ♝₂ | ♝₁ | ♝₁ | * |

>| ♝₂ | * | ♝₁ | ♝₂ |
>|---|---|---|---|
>| * | * | * | * |
>| * | ♝₁ | * | * |
>| * | * | ♝₂ | * |
>| ♝₂ | ♝₁ | ♝₁ | * |

>| ♝₂ | * | ♝₁ | ♝₂ |
>|---|---|---|---|
>| * | * | * | * |
>| * | ♝₁ | * | ♝₂ |
>| * | * | * | * |
>| ♝₂ | ♝₁ | ♝₁ | * |

>| ♝₂ | * | ♝₁ | ♝₂ |
>|---|---|---|---|
>| * | * | * | * |
>| * | * | * | ♝₂ |
>| * | * | ♝₁ | * |
>| ♝₂ | ♝₁ | ♝₁ | * |

>| ♝₂ | * | ♝₁ | ♝₂ |
>|---|---|---|---|
>| * | * | ♝₂ | * |
>| * | * | * | * |
>| * | * | ♝₁ | * |
>| ♝₂ | ♝₁ | ♝₁ | * |

>| ♝₂ | * | ♝₁ | ♝₂ |
>|---|---|---|---|
>| * | * | ♝₂ | * |
>| * | * | * | * |
>| * | * | * | * |
>| ♝₂ | ♝₁ | ♝₁ | ♝₁ |

>| ♝₂ | ♝₂ | ♝₁ | ♝₂ |
>|---|---|---|---|
>| * | * | * | * |
>| * | * | * | * |
>| * | * | * | * |
>| ♝₂ | ♝₁ | ♝₁ | ♝₁ |
>> **Aqui tenemos el tercer alfil llegando a su destino**

>| ♝₂ | ♝₂ | * | ♝₂ |
>|---|---|---|---|
>| * | * | * | ♝₁ |
>| * | * | * | * |
>| * | * | * | * |
>| ♝₂ | ♝₁ | ♝₁ | ♝₁ |

>| ♝₂ | ♝₂ | * | ♝₂ |
>|---|---|---|---|
>| * | * | * | ♝₁ |
>| * | * | * | * |
>| * | ♝₂ | * | * |
>| * | ♝₁ | ♝₁ | ♝₁ |

>| ♝₂ | ♝₂ | * | ♝₂ |
>|---|---|---|---|
>| * | * | * | * |
>| * | * | ♝₁ | * |
>| * | ♝₂ | * | * |
>| * | ♝₁ | ♝₁ | ♝₁ |

>| ♝₂ | ♝₂ | * | ♝₂ |
>|---|---|---|---|
>| * | * | * | * |
>| ♝₂ | * | ♝₁ | * |
>| * | * | * | * |
>| * | ♝₁ | ♝₁ | ♝₁ |

>| ♝₂ | ♝₂ | * | ♝₂ |
>|---|---|---|---|
>| * | * | * | * |
>| ♝₂ | * | * | * |
>| * | ♝₁ | * | * |
>| * | ♝₁ | ♝₁ | ♝₁ |

>| ♝₂ | ♝₂ | * | ♝₂ |
>|---|---|---|---|
>| * | ♝₂ | * | * |
>| * | * | * | * |
>| * | ♝₁ | * | * |
>| * | ♝₁ | ♝₁ | ♝₁ |

>| ♝₂ | ♝₂ | * | ♝₂ |
>|---|---|---|---|
>| * | ♝₂ | * | * |
>| * | * | * | * |
>| * | * | * | * |
>| ♝₁ | ♝₁ | ♝₁ | ♝₁ |

>| ♝₂ | ♝₂ | ♝₂ | ♝₂ |
>|---|---|---|---|
>| * | * | * | * |
>| * | * | * | * |
>| * | * | * | * |
>| ♝₁ | ♝₁ | ♝₁ | ♝₁ |

> Como vemos se cumplio con lo pedido de intercambiar de lugar los alfiles, siendo este el algoritmo mas sencillo y con menos movimientos de todos.