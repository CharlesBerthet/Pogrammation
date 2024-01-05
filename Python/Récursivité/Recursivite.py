def u_iter(n):
    u=2
    for i in range(1,n+1):
        u=2*u-3
    return u


def u_rec(n):
    if n==0:
        return 2
    else:
        return 2*u_rec(n-1)-3


