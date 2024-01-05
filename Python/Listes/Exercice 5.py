#Retournement de valeur dans une liste

def retournement(pile, k):
    pile2 = []
    pile3 = []
    taille = len(pile)
    for i in range(k, taille):
        pile2.append(pile[i])
    for i in range(k, taille):
        pile3=[pile[i]]+pile3
    return pile2 + pile3


#Cherche le maximum 

def maximum(liste):
    maxi = liste[0]
    for val in liste:
        if val > maxi:
            maxi = val
    return maxi


#Triage de crêpes

def Tri_crêpes(pile):
    taille=len(pile)
    for i in range(taille):
        maxi=maximum(pile[i:])
        ind=pile.index(maxi)
        pile=retournement(pile, ind)
        pile=retournement(pile, i)
    return pile



