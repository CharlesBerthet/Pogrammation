a=float(input("Donnez une première valeur : "))
b=float(input("Donnez une deuxième valeur : "))
c=float(input("Donnez une troisième valeur : "))
if a > b and a > c :
    print(a," est la plus grande valeur donnée !")

elif b > a and b > c :
    print(b," est la plus grande valeur donnée !")

elif c > a and c > b :
    print(c," est la plus grande valeur donnée !") 

else :
    print("try again error")