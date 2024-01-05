def compte(chaine):
    cpt=0
    for i in chaine:
        if i=='a':
            cpt+=1
    return cpt


def compte_recu(chaine):
    if len(chaine)==0:
        return 0
    else:
        if chaine[0]=='a':
            return 1+compte_recu(chaine[1:])
        else:
            return compte_recu(chaine[1:])


