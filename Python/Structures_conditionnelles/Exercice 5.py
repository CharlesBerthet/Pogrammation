a=int(input("Donnez moi une année : "))
if a%4 == 0 and a%100 != 0 :
    print("c'est une année bissextile !")

elif a%400 == 0 :
    print("C'est une année bissextile !")

else :
    print("Ce n'est pas une année bissextile !")