def non_recu(n):
    u=0
    for i in range(1,n+1):
        u = u + i
    return u


def recu(n):
    if n==0:
        return 0
    else:
        return n+recu(n-1)



