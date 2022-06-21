def maior_elemento(lista):
    maior = 0
    for i in range(len(lista)):
        if lista[maior] < lista[i]:
            maior = i
    return maior
