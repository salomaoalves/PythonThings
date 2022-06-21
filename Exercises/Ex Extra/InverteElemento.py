def inverte_seq():
    i = 0
    a = [int(input("Digite um numero: "))]
    while a[i] != 0:
        a.append(int(input("Digite um numero: ")))
        i += 1
    del a[len(a)-1]
    for i in range(len(a)-1,-1,-1):
        print(a[i])
    
            
