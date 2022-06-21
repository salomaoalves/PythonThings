def conta_letras(string,contar="vogais"):
    qtdVogais = 0
    vogais = ["a","e","i","o","u"]
    for i in range(len(string)):
        if string[i] in vogais:
            qtdVogais += 1
    if contar == "vogais":
        return qtdVogais
    elif contar == "consoantes":
        return len(string)-qtdVogais
