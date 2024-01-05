a=float(input("coeff de x2 : "))
b=float(input("coeff de x : "))
c=float(input("coeff constant : "))

if a != 0 :
    delta = b**2-4*a*c

    if delta < 0 :
        print("Le trinôme ne possède aucune racine")

    elif delta == 0 :
        print("Le trinôme possède 1 racine")

    else :
        print("Le trinôme possède 2 racines")

else : 

    if b == 0 :

        if c == 0 :
            print("Le trinôme possède une infinité de racines")

        else :
            print("Le trinôme ne possède aucune racine")
            
    else :
        print("Le trinôme possède 1 racine")