def busca(lista, elemento):
    pri = 0
    ult = len(lista)-1
    while pri <= ult:
        meio = (pri+ult)//2
        print(meio)
        if lista[meio] == elemento:
            return meio
        elif elemento < lista[meio]:
            ult = meio - 1
        else:
            pri = meio + 1
    return False
