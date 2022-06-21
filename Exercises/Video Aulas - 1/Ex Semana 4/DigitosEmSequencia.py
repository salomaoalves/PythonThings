number = int(input("Digite um número ineiro: "))
cont = resto = resto2 = 0

while number != 0:
    resto = number%10
    number = number//10
    resto2 = number%10
    if resto == resto2:
        print("sim")
        cont += 1
        break

if cont == 0:
    print("não")
