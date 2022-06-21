def imprime_mat(lista):
    nro_linha = len(lista)
    nro_col = len(lista[0])
    for i in range(nro_linha):
        for j in range(nro_col):
            print(lista[i][j],end=" ")
        print()
