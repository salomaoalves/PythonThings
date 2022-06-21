def remove_repetidos(lista):
    i = 0
    vet = []
    size = len(lista)
    while i < size:
        cont = 0
        j = 0
        tam = size
        var = lista[i]
        while tam != 0:
            tam -= 1
            var2 = lista[j]
            if (var == var2):
                cont += 1
                if cont>1:
                    del lista[j]
                    size -= 1
            j += 1
        i += 1
    print(lista)
    a = lista.sort()
    print(a)
