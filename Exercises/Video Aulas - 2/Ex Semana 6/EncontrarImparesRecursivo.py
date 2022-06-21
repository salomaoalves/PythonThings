import pygame
def encontra_impares(lista):
    a = []
    if lista == []:
        return []
    if lista[0]%2 == 0:
        return encontra_impares(lista[1:])
    else:
        return a.extend([lista[0]] + encontra_impares(lista[1:]))
