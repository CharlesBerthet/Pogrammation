from random import *

a = 0


def lancer(nbr_lancer):
    b = 0
    for i in range (nbr_lancer):
        a = randint(1, 6)
        if a == 6 :
            b = b + 1
        print('Le resultat est : ',a)
    print('Nombre de 6 obtenue = ',b)

print(lancer(1114))


