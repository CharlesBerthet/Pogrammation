from math import*

n = int(input("Entrer un entier supérieur à 1: "))
fibo = [0]*(n)
fibo[0] = 1
fibo[1] = 1
for i in range(2,n):
  fibo[i] = fibo[i-1] + fibo[i-2]
print(fibo)



