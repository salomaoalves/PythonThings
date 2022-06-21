def maiusculas(string):
    vet = ""
    for i in range(len(string)):
        if(ord(string[i]) >= ord("A") and ord(string[i]) <= ord("Z")):
            vet += string[i]
    return vet
