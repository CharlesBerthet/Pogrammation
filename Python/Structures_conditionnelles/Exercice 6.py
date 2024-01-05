a=float(input("Donnez moi 3 notes, la première : "))
b=float(input("La deuxième : "))
c=float(input("La troisième : "))
moy=(a+b+c)/3

if moy >= 14 :
    print("Bon travail !")

elif 10 <= moy < 16:
    print("Ensemble convenable")

elif moy < 10 :
    print("Insuffisant")

else :
    print("try again error")