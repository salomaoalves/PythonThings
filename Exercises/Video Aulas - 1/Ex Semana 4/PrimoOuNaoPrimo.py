number = int(input("Digite um número inteiro: "))
metade = number//2
cont = 0
i = 2

while i <= metade:
    if number%i == 0:
        cont += 1
    i += 1

if cont == 0:
    print("primo")
else:
    print("não primo")
