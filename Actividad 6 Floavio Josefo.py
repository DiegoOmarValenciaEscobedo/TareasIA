personas = int(input("Ingrese el numero de personas: "))
posicion = 1

def esExponenteDeDos(numero):
    exponente = 0
    while (2 ** exponente <= numero):
        if (2 ** exponente == numero):
            return True
        exponente += 1
    return False

for i in range(personas):
    if (esExponenteDeDos(i+1)):
        posicion = 1
    else:
        posicion += 2
    print('vuelta', i+1, 'posicion', posicion)
print('La persona que se salva es la', posicion)