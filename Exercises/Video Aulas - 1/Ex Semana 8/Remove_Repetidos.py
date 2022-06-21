def remove_repetidos(lista):
    cont = 0
    size = len(lista) - 1
    for i in lista:
        j = i + 1
        while cont <= size:
            cont += 1
            if i == lista[j]:
                del lista[j]
                size -= 1
            else:
                j += 1
    
    return lista
