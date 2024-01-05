# Cherche le minimum

def minimum(liste):
    mini = liste[0]
    for val in liste:
        if val < mini:
            mini = val
    return mini


#Cherche le maximum

def maximum(liste):
    maxi = liste[0]
    for val in liste:
        if val > maxi:
            maxi = val
    return maxi

