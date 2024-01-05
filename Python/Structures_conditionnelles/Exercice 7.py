a=str(input("Donnez moi 3 mots différents, le premier : "))
b=str(input("Le deuxième : "))
c=str(input("Le troisème : "))


if a < b and a < c :
    if b < c :
        print("Les noms sont classés dans l'ordre alphabétique : ",a ,b ,c)

    elif c < b :
        print("Les noms sont classés dans l'ordre alphabétique : ",a ,c ,b)

if b < a and b < c :
    if a < c :
        print("Les noms sont classés dans l'ordre alphabétique : ",b ,a ,c)

    elif c < a :
        print("Les noms sont classés dans l'ordre alphabétique : ",b ,c ,a)

if c < a and c < b :
    if a < b :
        print("Les noms sont classés dans l'ordre alphabétique : ",c ,a ,b)

    elif b < a :
        print("Les noms sont classés dans l'ordre alphabétique : ",c ,b ,a)


