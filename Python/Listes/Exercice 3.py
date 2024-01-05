# Tri avec le minimum

def minimum(liste):
    mini = liste[0]
    for val in liste:
        if val < mini:
            mini = val

def tri(liste):
    liste_triée = []
    for i in range(len(liste)):
        val = minimum(liste)
        liste_triée+=[val]
        liste.remove(val)
    return liste_triée


# Tri à bulles

def tribulles(liste):
    for i in range(len(liste)):
        for j in range(len(liste)-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

