nombre1 = int(input('Entrez le premier nombre: '))
nombre2 = int(input('Entrez le deuxième nombre: '))
nombre3 = int(input('Entrez le troisième nombre: '))

def min3nombres(nombre1, nombre2, nombre3):
    if (nombre1 < nombre2 and nombre1 < nombre3):
        return nombre1
    elif (nombre2 < nombre1 and nombre2 < nombre3):
        return nombre2
    elif (nombre3 < nombre2 and nombre3 < nombre1):
        return nombre3
    

print(min3nombres(nombre1, nombre2, nombre3))


