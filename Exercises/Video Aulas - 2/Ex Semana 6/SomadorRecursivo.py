def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        soma = lista[0] + soma_lista(lista[1:])
    return soma
