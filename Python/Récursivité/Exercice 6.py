def mystere(a, b):
    if b == 1:
        return a
    else :
        return a + mystere(a, b - 1)



        