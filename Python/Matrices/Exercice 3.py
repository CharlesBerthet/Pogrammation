n =int(input('entrez nombre : '))
P=[[0 for i in range(n)] for i in range(n)]
for i in range(n):
    P[i][0] = 1
for i in range(1,n):
    for j in range(1,n):
        P[i][j]=P[i-1][j-1]+P[i-1][j]

for ligne in P:
    print(ligne)



