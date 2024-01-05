from math import *

nbr=int(input("Donnez moi un nombre : "))
fct = 1

for i in range(1,nbr+1):
    fct = 1 - exp(-2*nbr)

print(fct)

