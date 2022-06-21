class Fila:
    def __init__(self,qtd):
        self.fila = [0]*qtd
        self.ini = 0
        self.fim = 0

    def insere(self,ele):
        if self.cheia():
            print("Fila esta cheia")
            return
        self.fila[self.fim] = ele
        self.fim += 1
        if self.fim == len(self.fila):
            self.fim = 0

    def remove(self):
        if self.vazia():
            print("Fila esta vazia")
            return
        self.ini += 1
        if self.ini == len(self.fila):
            self.ini = 0

    def cheia(self):
        if (self.fim+1)%(len(self.fila)) == self.ini:
            return True
        else:
            return False

    def vazia(self):
        if self.ini == self.fim:
            return True
        else:
            return False

    def imprimi(self):
        i = self.ini
        if self.vazia():
            print("A fila esta vazia ou foi destruída")
        while self.fila[i] != 0:
            print(self.fila[i],end=" ")
            i += 1
            if i == len(self.fila):
                i = 0

    def destroi(self):
        self.ini = self.fim = 0
        for i in range(len(self.fila)):
            self.fila[i] = 0
        
