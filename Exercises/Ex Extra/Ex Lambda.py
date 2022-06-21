def main():
    square = lambda x: x**2#criada por lambda
    lista_por_lambda = [square(x) for x in range(11)]
    
    lista_compreensao = [i**2 for i in range(11)]#criada por lista de compreensao

    pares = lambda x: x if x%2 == 0 else None#filtra apenas os pares
    sopares = list(filter(pares,lista_compreensao))
    print(sopares)

    divide_por_dois = lambda x: x/2#mapeia cada elemento dividindo-o por dois
    metade = list(map(divide_por_dois,sopares))
    print(metade)
