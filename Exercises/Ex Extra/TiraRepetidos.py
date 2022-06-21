import Ordenador
def remove_repetidos(lista):
    i = 0
    l = Ordenador.quickSort(lista)
    while i+1 != len(l):
        if l[i] == l[i+1]:
            del l[i]
        else:
            i += 1
    return l
