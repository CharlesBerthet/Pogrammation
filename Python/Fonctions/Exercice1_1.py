nombre1 = int(input('Entrez le premier nombre: '))
nombre2 = int(input('Entrez le deuxième nombre: '))

def min2nombres(nombre1, nombre2):
    if (nombre1 > nombre2):
        return nombre2
    elif (nombre2 > nombre1):
        return nombre1

print(min2nombres(nombre1, nombre2))


