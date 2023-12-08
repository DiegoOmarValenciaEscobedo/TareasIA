# Problema de los misioneros.

Este problema tambien nos pide encontrar los estados por los que pasa para llegar a la solución, nos plantea lo siguiente, tenemos 3 misioneros que se perdieron en una isla, se encontraron con 3 canivales, despues de esto querian cruzar un rio, pero solo habia una balsa en donde cabian 2 personas, el problema es que no se pueden quedar de un lado mas canivales que misioneros ya que si eso pasa se los comeran, lo que nos pide es encontrar una forma de pasar a todos del otro lado del rio sin que en ningun momento se queden mas canivales de cualquier lado.

La representación de la situacion es asi:
>🧑‍🦳🧑‍🦳🧑‍🦳 👨🏿👨🏿👨🏿 | ⛵ | ____

De forma que podemos empezar a resolver o simular la posible solucion, teniendo en cuenta las unicas 2 reglas

- Solo caben 2 personas en el bote y una tiene que manejarlo a fuerzas, asi que uno tiene que regresarse manejandolo.
- En nungun momento se pueden quedar mas canivales que monjes de ningun lado.

**Posicion inicial:**
>🧑‍🦳🧑‍🦳🧑‍🦳 👨🏿👨🏿👨🏿 | ⛵ | ____

**Viaje 1:** En el primer viaje se iria un monje y un canival, del otro lado se queda el canival y se regresa manejando el bote el monje.
>🧑‍🦳🧑‍🦳 👨🏿👨🏿 | ⛵👨🏿🧑‍🦳 | ____
>|-----------|---------|-----|
>🧑‍🦳🧑‍🦳 👨🏿👨🏿 |  ⛵🧑‍🦳  | 👨🏿 |
>🧑‍🦳🧑‍🦳🧑‍🦳 👨🏿👨🏿 |  ⛵  | 👨🏿 |

**Viaje 2:** En este viaje se irian dos canivales, del otro lado se queda uno de ellos y otro se regresa.
>🧑‍🦳🧑‍🦳🧑‍🦳 |  ⛵👨🏿👨🏿  | 👨🏿 |
>|-----------|---------|-----|
>🧑‍🦳🧑‍🦳🧑‍🦳 |  ⛵👨🏿  | 👨🏿👨🏿 |
>🧑‍🦳🧑‍🦳🧑‍🦳 👨🏿 |  ⛵  | 👨🏿👨🏿 |

**Viaje 3:** En este viaje se irian dos mojes, del otro lado se queda 1 monje y se regresa en el bote un canival y un monje.
>🧑‍🦳👨🏿 |  ⛵🧑‍🦳🧑‍🦳  | 👨🏿👨🏿 |
>|-----|------------|-------|
>🧑‍🦳👨🏿 |  ⛵👨🏿🧑‍🦳  | 👨🏿🧑‍🦳 |
>🧑‍🦳👨🏿👨🏿🧑‍🦳 |  ⛵  | 👨🏿🧑‍🦳 |

**Viaje 4:** En este viaje se irian dos mojes, del otro lado se quedan los monjes y se regresa en el bote un canival.
>👨🏿👨🏿 |  ⛵🧑‍🦳🧑‍🦳  | 👨🏿🧑‍🦳 |
>|-----|------------|-------|
>👨🏿👨🏿 |  ⛵👨🏿  | 🧑‍🦳🧑‍🦳🧑‍🦳 |
>👨🏿👨🏿👨🏿 |  ⛵  | 🧑‍🦳🧑‍🦳🧑‍🦳 |

**Viaje 5:** En este viaje se irian dos canivales, del otro lado se queda uno y se regresa en el bote un canival.
>👨🏿 |  ⛵👨🏿👨🏿  | 🧑‍🦳🧑‍🦳🧑‍🦳 |
>|-----|------------|-------|
>👨🏿 |  ⛵👨🏿  | 🧑‍🦳🧑‍🦳🧑‍🦳👨🏿 |
>👨🏿👨🏿 |  ⛵  | 🧑‍🦳🧑‍🦳🧑‍🦳👨🏿 |

**Viaje 6:** En este viaje se irian dos mojes, asi quedan todos del otro lado y se cumple lo pedido.
>👨🏿👨🏿 |  ⛵  | 🧑‍🦳🧑‍🦳🧑‍🦳👨🏿 |
>|-----|------------|-------|
> ____ |  ⛵👨🏿👨🏿  | 🧑‍🦳🧑‍🦳🧑‍🦳👨🏿 |
> ____ |  ⛵  | 👨🏿👨🏿👨🏿🧑‍🦳🧑‍🦳🧑‍🦳 |


