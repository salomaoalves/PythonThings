def ordenada(lista):
    ordenada = ehOrd(lista)
    return ordenada

def ehOrd(lista):
    fim = len(lista)
    for i in range(fim-1):
        pos_min = i
        for j in range(i+1,fim):
            if lista[j] < lista[pos_min]:
                return False
    return True
