def primo():
    qtd = int(input("Quantas numeros?"))
    while qtd > 0:
        cont = 0
        a = int(input("Numeros: "))
        m = a/2
        met = int(m)
        while met > 1:
            if a%met == 0:
                cont += 1
            met -= 1
        if cont != 0:
            print (False)
        else:
            print (True)
        qtd -= 1

    
