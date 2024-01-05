paquet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# Algorithme mélange des cartes dans le paquet

def melange(paq):
    from random import randint
    for i in range(50):
        ind1 = randint(0, 19)
        ind2 = randint(0, 19)
        temp=paq[ind1]
        paq[ind1]=paq[ind2]
        paq[ind2]=temp
    return paq


# Algorithme de distribution des cartes

def distribution(paq):
    paquetA = [0 for i in range(20)]
    paquetB = [0 for i in range(20)]
    for i in range(0, 10):
        paquetA[i] = paq[2*i]
        paquetB[i] = paq[2*i+1]
    return paquetA, paquetB


# Algorithme OTUN

def otun(paq):
    res=[0 for i in range(20)]
    for i in range(0, 19):
        res[i] = paq[i+1]
    res[19] = 0
    return res


# Algorithme retour zero

def indzero(paq):
    for i in range(20):
        if paq[i] == 0:
            return i 
    return 20


# Algorithme partie
