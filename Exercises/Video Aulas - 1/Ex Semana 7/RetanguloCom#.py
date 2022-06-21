l = int(input("difite a largura: "))
a = int(input("difite a altura: "))

while a >= 1:
    cont = 1
    while cont <= l:
        print("#",end = "")
        cont += 1
    a -= 1
    print()
