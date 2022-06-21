def maior_primo(x):
    resp = éPrimo(x)
    if resp == "true":
        return x
    else:
        while resp == "false":
            x -= 1
            resp = éPrimo(x)
        return x

def éPrimo(k):
    i = 2
    while i != (k//2):
        if k%i == 0:
            return "false"
        i += 1
    return "true"
