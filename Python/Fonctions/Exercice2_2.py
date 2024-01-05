palin=str(input("Donnez un mot : "))

def verlan (verlan):
    return verlan [::-1]

print(verlan(palin))

if verlan(palin) == palin :
    print("C'est un palindrome")
else :
    print("Ce n'est pas un palindrome")



