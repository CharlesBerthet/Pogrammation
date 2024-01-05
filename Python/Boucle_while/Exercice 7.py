nbr =int(input("Écris un nombre entier positif : "))

print("Le programme est en train de vérifier si ce nombre est premier...")

i = 2
while i < nbr and nbr % i != 0:
    i = i + 1

if i == nbr:
    print("Le nombre", nbr, "est premier !")
else:
    print("Ce n'est pas un nombre premier.")


    
