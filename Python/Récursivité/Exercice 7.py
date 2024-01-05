def Pascal(i, j):
    if j == 0 or i == j:
        return 1
    elif j > i :
        return 0
    else :
        return Pascal(i-1, j-1)+ Pascal(i-1, j)



for i in range(5):
    ligne=[]
    for j in range(5):
        ligne.append(Pascal(i, j))
    print(ligne)




