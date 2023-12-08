import random

H = int(input("Ingresa la altura del mapa: "))
W = int(input("Ingresa el ancho del mapa: "))

mapa = []

for i in range(H):
    fila = []
    for j in range(W):
        valor = int(random.uniform(0, 1.2))
        fila.append(valor)
    mapa.append(fila)

print("Este es el mapa:")
for fila in mapa:
    for celda in fila:
        print("■" if celda == 1 else "·", end="  ")
    print()

# Buscar islas metodo recursivo
def funcionRecursiva(i, j):
    if i < 0 or i >= H or j < 0 or j >= W:
        return
    if mapa[i][j] != 1:
        return
    mapa[i][j] = 2
    funcionRecursiva(i - 1, j)
    funcionRecursiva(i + 1, j)
    funcionRecursiva(i, j - 1)
    funcionRecursiva(i, j + 1)

islas = 0
for i in range(H):
    for j in range(W):
        if mapa[i][j] == 1:
            islas += 1
            funcionRecursiva(i, j)

print("Hay", islas, "islas existentes")

# Buscar islas metodo iterativo
islas = 0
for i in range(H):
    for j in range(W):
        if mapa[i][j] == 1:
            islas += 1
            mapa[i][j] = 2

print("Hay", islas, "islas existentes")