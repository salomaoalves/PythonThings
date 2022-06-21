def fatorial(x):
    fator = 1
    while x != 0:
        fator = fator * x
        x = x - 1
    return fator

n = int(input("O 'n' do numero binomial: "))
k = int(input("O 'k' do numero binomial: "))

num = fatorial(n)
den1 = fatorial(k)
den2 = fatorial(n-k)

binomial = num / (den1 * den2)

print("A resposta é ",binomial)
