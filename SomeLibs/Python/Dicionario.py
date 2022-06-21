class Dicionario:
    def __init__(self):
        self.dic = { }
        
    def cria_dic(self):
        while True:
            erro = 0#nao ha erro
            try:
                chave = int(input("Digite a chave (-1 para sair): "))
            except:
                print("Colocar uma chave inteiro")
                erro = 1#ha erro
            if not erro:
                if chave == -1:
                    break
                else:
                    while True:
                        erro = 0 #nao ha erro
                        try:
                            valor = int(input("Digite o valor: "))
                        except:
                            print("Colocar um valor inteiro")
                            erro = 1#ha erro
                        if not erro:
                            self.add_ele(chave,valor)
                            break
        print()

    def add_ele(self,chave,valor):
        self.dic[chave] = valor
        print()

    def remove_ele(self,chave):
        del self.dic[chave]
        print()

    def imprimir(self):
        print(self.dic.items())
        for i in self.dic.keys():
            print(i, "=", self.dic[i])
        print()

    def busca_chave(self,key):
        if key in self.dic.keys():
            print("A chave:",key,"tem valor",self.dic[key])
        else:
            print("Nao existe a chave",chave)
        print("Chaves:",self.dic.keys())
        print()

    def busca_valor(self,valor):
        if valor in self.dic.values():
            print(True,",assim, o valor dado existe")
        else:
            print(False,",assim, o valor dado n existe")
        print("Valores:",self.dic.values())
        print()

    def dado_existente(self,chave,valor):
        if (chave,valor) in self.dic.items():
            print(True,",assim, existe esse dado")
        else:
            print(False,",assim, n existe esse dado")
        print()

if __name__ == '__main__':
    d = Dicionario()
    d.cria_dic()
    d.imprimir()
    d.add_ele(5,200)
    d.imprimir()
    d.remove_ele(1)
    d.imprimir()
    d.busca_chave(2)
    d.imprimir()
    d.busca_valor(200)
    d.imprimir()
    d.dado_existente(5,200)
    d.imprimir()