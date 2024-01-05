def repartition(liste):
    pair = []
    impair = []
    for val in liste :
        if val%2 == 0 :
            pair.append(val)
        else :
            impair.append(val)
    return pair, impair

