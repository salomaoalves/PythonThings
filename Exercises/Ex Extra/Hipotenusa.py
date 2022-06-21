def soma_hipo(n):
    i = cont = 0
    while i<=n:
        if(e_hipo(i)):
            cont += i
        i += 1
    return cont

def e_hipo(h):
    
