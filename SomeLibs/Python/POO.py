class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def more_info(self):
        print("Faço nada")


class Juridica(Pessoa):
    def __init__(self,nome,idade,cnpj):
        super().__init__(nome,idade)
        self.cnpj = cnpj
        
    def more_info(self):
	    print("CNPJ: " + self.cnpj)

class Fisica(Pessoa):
    def __init__(self,nome,idade,cpf):
        super().__init__(nome,idade)
        self.cpf = cpf
        
    def more_info(self):
	    print("CPF: "+self.cpf)

class Empresa:
    def __init__(self,pessoa):
        if type(pessoa) == Juridica:
            self.pessoa = pessoa
            print("Empresa criada")
        else:
            print("Pedido negado")
            raise Exception


if __name__ == '__main__':
    p1 = Juridica('Cruzeiro','99','11111')
    p2 = Fisica('salomao','20','22222')
    try:
        e1 = Empresa(p1)
    except Exception as e:
        print("Empresa nao foi criada")
    try:
        e2 = Empresa(p2)
    except Exception as e:
        print("Empresa nao foi criada")
    p1.more_info()
    p2.more_info() 
