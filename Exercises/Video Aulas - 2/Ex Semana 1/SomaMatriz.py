def soma_matrizes(m1,m2):
    l1 = len(m1)
    c1 = len(m1[0])
    l2 = len(m2)
    c2 = len(m2[0])
    if (l1 != l2 or c1 != c2):
        return False
    else:
        resultante = []
        for i in range(l1):
            linha = []
            for j in range(c1):
                valor = m1[i][j]+m2[i][j]
                linha.append(valor)
            resultante.append(linha)
        return resultante
