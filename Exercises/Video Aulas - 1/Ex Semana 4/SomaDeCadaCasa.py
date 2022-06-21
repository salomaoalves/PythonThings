number = int(input("Digite um número inteiro: "))
valor = 0

while number != 0:
    soma = number%10
    number = number//10
    valor = valor + soma

print(valor)
