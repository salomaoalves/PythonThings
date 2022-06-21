L = int(input("difite a largura: "))
a = int(input("difite a altura: "))
altura = 1

while altura <= a:
    largura = 1
    while largura <= L:
        if altura == 1 or altura == a:
            print("#",end = "")
        elif largura == 1 or largura == L:
            print("#", end = "")
        else:
            print(end = " ")
        largura += 1
    print()
    altura += 1
