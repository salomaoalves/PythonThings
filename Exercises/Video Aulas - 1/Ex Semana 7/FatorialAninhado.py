vezes = int(input("Quantos numero voce deseja calcular o fatorial?"))

while vezes > 0:
    a = int(input("Numero: "))
    fat = 1
    while a > 0:
        fat *= a
        a -= 1
    print(fat)
    vezes -= 1
