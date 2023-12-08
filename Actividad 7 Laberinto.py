encontrado = False
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
#empieza en laberinto[1][0]

def busqueda(x,y):
    global encontrado
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