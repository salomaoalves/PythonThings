def n_primos(x):
    lista = []
    i = 2
    while i <= x:
        if(ePrimo(i)):
            lista.append(i)
        i += 1
    return len(lista)

def ePrimo(x):
    div = 2
    if x==2:
        return True
    while div <= 2:
        if(x % div == 0):
            return False
        div += 1
    return True
