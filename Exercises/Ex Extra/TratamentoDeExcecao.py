def main():
    banco = {}
    contador_chave = 1
    nome, idade = None, None
    print("Obs: digite exit para sair")
    while True:
        if not nome:
            nome = input("Nome: ")
            if nome == 'Exit' or nome == 'exit':
                print(imprime_banco(banco))
                return 'Sucesso'
        try:
            idade = int(input("Idade: "))
        except:
            print("A idade de ser um inteiro")
        finally:
            if idade:
                banco[contador_chave] = [nome,idade]
                contador_chave += 1
                nome, idade = None, None

def imprime_banco(b):
    for chave in b:
        print("\nChave: "+str(chave)+" -> Nome: "+str(b[chave][0])+" -> Idade: "+str(b[chave][1]))
