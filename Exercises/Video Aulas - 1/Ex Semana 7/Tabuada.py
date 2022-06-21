linha = 1
coluna = 1
while linha <= 9:
    while coluna <= 9:
        print(coluna*linha, end = "\t|\t")
        coluna += 1
    linha += 1
    coluna = 1
    print()
