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
